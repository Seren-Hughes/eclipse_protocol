from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product, DigitalVariant
from decimal import Decimal
import uuid

# Create your models here.

class Order(models.Model):
    """
    Core order model storing both foreign key references and snapshotted data.
    
    Design philosophy:
    - FK references for relationships (user, addresses) 
    - Snapshotted fields for historical data integrity
    - Order data must remain intact even if referenced models change
    """
    
    # Order identification
    order_number = models.CharField(max_length=32, unique=True, editable=False)
    
    # Relationships (nullable for data integrity)
    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='orders'
    )
    
    # Order lifecycle
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Status tracking
    PAYMENT_PENDING = 'pending'
    PAYMENT_PAID = 'paid'
    PAYMENT_FAILED = 'failed'
    PAYMENT_REFUNDED = 'refunded'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_PAID, 'Paid'),
        (PAYMENT_FAILED, 'Failed'),
        (PAYMENT_REFUNDED, 'Refunded'),
    ]
    
    DELIVERY_PENDING = 'pending'
    DELIVERY_SENT = 'sent'
    DELIVERY_DELIVERED = 'delivered'
    
    DELIVERY_STATUS_CHOICES = [
        (DELIVERY_PENDING, 'Pending'),
        (DELIVERY_SENT, 'Sent'),
        (DELIVERY_DELIVERED, 'Delivered'),
    ]
    
    payment_status = models.CharField(
        max_length=20, 
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_PENDING
    )
    delivery_status = models.CharField(
        max_length=20,
        choices=DELIVERY_STATUS_CHOICES, 
        default=DELIVERY_PENDING
    )
    
    # Snapshotted customer details (preserve at time of order)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    
    # Billing address snapshot
    street_address_1 = models.CharField(max_length=255)
    street_address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    
    # Business logic flags
    subscription_renewal = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-order_date']
    
    def __str__(self):
        return f"Order {self.order_number}"
    
    def save(self, *args, **kwargs):
        """Auto-generate order number on creation"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def _generate_order_number(self):
        """Generate unique order number with prefix"""
        return f"EP{uuid.uuid4().hex[:8].upper()}"
    
    @property
    def item_count(self):
        """Total number of items in this order"""
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    """
    Individual items within an order.
    
    Stores both references and snapshotted data to preserve
    order history even if products/prices change later.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    
    # Product reference (PROTECT ensures we can't delete products with orders)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    variant = models.ForeignKey(DigitalVariant, on_delete=models.PROTECT, null=True, blank=True)
    
    # Snapshotted product data (preserve pricing at time of purchase)
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=64)
    variant_details = models.CharField(max_length=255, blank=True)  # "PC Ultimate Edition"
    
    # Order specifics
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.variant_details:
            return f"{self.product_name} - {self.variant_details} x{self.quantity}"
        return f"{self.product_name} x{self.quantity}"
    
    def save(self, *args, **kwargs):
        """Auto-calculate total price on save"""
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)