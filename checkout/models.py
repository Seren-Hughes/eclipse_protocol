import uuid
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models

from catalog.models import DigitalVariant, Product

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
    stripe_pid = models.CharField(max_length=254, null=True, blank=True) # Stripe PaymentIntent ID for tracking
    original_cart = models.TextField(null=True, blank=True) # JSON snapshot of cart at purchase time

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


class Payment(models.Model):
    """
    Payment tracking for Stripe integration.
    
    Stores payment metadata and links to Stripe's PaymentIntent system.
    Separate from Order to allow multiple payment attempts per order.
    """
    
    # Payment identification
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    transaction_id = models.CharField(max_length=255, unique=True)  # Stripe PaymentIntent ID
    
    # Payment lifecycle
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Stripe payment status tracking (maps directly to Stripe's PaymentIntent status)
    REQUIRES_PAYMENT_METHOD = 'requires_payment_method'
    REQUIRES_CONFIRMATION = 'requires_confirmation'  
    REQUIRES_ACTION = 'requires_action'
    PROCESSING = 'processing'
    REQUIRES_CAPTURE = 'requires_capture'
    CANCELED = 'canceled'
    SUCCEEDED = 'succeeded'
    
    STATUS_CHOICES = [
        (REQUIRES_PAYMENT_METHOD, 'Requires Payment Method'),
        (REQUIRES_CONFIRMATION, 'Requires Confirmation'),
        (REQUIRES_ACTION, 'Requires Action'),
        (PROCESSING, 'Processing'),
        (REQUIRES_CAPTURE, 'Requires Capture'),
        (CANCELED, 'Canceled'),
        (SUCCEEDED, 'Succeeded'),
    ]
    
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=REQUIRES_PAYMENT_METHOD
    )
    
    # Additional Stripe metadata
    stripe_charge_id = models.CharField(max_length=255, blank=True)
    failure_reason = models.TextField(blank=True)

    class Meta:
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.get_status_display()}"
    
    @property
    def is_successful(self):
        """Check if payment completed successfully"""
        return self.status == self.SUCCEEDED
    


class LicenseKey(models.Model):
    """
    Digital license keys for purchased products.
    
    Generated after successful payment and delivered via email.
    Supports different platforms and tracks delivery status.
    """
    
    # Key ownership and origin
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='license_keys')
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='license_keys')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    variant = models.ForeignKey(DigitalVariant, on_delete=models.PROTECT, null=True, blank=True)
    
    # License details
    key_code = models.CharField(max_length=64, unique=True)
    
    # Platform alignment with DigitalProduct/DigitalVariant
    PC = 'PC'
    XBOX = 'Xbox'
    PLAYSTATION = 'PlayStation'
    NINTENDO = 'Nintendo'
    
    PLATFORM_CHOICES = [
        (PC, 'PC'),
        (XBOX, 'Xbox'),
        (PLAYSTATION, 'PlayStation'), 
        (NINTENDO, 'Nintendo'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default=PC)
    
    # Delivery tracking
    email_sent = models.BooleanField(default=False)
    email_sent_at = models.DateTimeField(null=True, blank=True)
    download_count = models.PositiveIntegerField(default=0)
    last_downloaded = models.DateTimeField(null=True, blank=True)
    
    # Key lifecycle
    KEY_ACTIVE = 'active'
    KEY_USED = 'used'
    KEY_REVOKED = 'revoked'
    KEY_EXPIRED = 'expired'
    
    KEY_STATUS_CHOICES = [
        (KEY_ACTIVE, 'Active'),
        (KEY_USED, 'Used'),
        (KEY_REVOKED, 'Revoked'),
        (KEY_EXPIRED, 'Expired'),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=KEY_STATUS_CHOICES,
        default=KEY_ACTIVE
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),  # User's key history
            models.Index(fields=['key_code']),  # Key lookup
        ]
    
    def __str__(self):
        product_name = self.variant.product.name if self.variant else self.product.name
        variant_info = f" - {self.variant}" if self.variant else ""
        return f"{product_name}{variant_info} - {self.platform}"
    
    def mark_as_sent(self):
        """Mark license key as sent via email"""
        from django.utils import timezone
        self.email_sent = True
        self.email_sent_at = timezone.now()
        self.save(update_fields=['email_sent', 'email_sent_at'])
    
    def record_download(self):
        """Record a key download/redemption"""
        from django.utils import timezone
        self.download_count += 1
        self.last_downloaded = timezone.now()
        if self.download_count == 1:
            self.status = self.KEY_USED
        self.save(update_fields=['download_count', 'last_downloaded', 'status'])
    
    @property
    def is_redeemable(self):
        """Check if key can still be redeemed"""
        return self.status in [self.KEY_ACTIVE, self.KEY_USED]