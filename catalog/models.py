from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
import uuid

# Create your models here.

class Product(models.Model):
    """
    Base product model for all product types in the catalog.
    Supports digital games, in-game currency 
    (future scope physical merchandise and subscriptions can be added)
    """
    BASE_GAME = 'base_game'
    CURRENCY = 'currency'
    
    PRODUCT_TYPE_CHOICES = [
        (BASE_GAME, 'Base Game'),
        (CURRENCY, 'In-Game Currency'),
    ]

    # Core fields
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    sku = models.CharField(max_length=50, blank=True, unique=True)  # Auto-generated if empty
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Inventory and status
    is_active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False) # Featured products for homepage
    sort_order = models.IntegerField(default=0)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Auto-generate SKU if empty"""
        if not self.sku:
            # BG = BASE_GAME, CR = CURRENCY
            type_codes = {
                'base_game': 'BG',
                'currency': 'CR',
            }
            type_code = type_codes.get(self.product_type, 'XX')
            self.sku = f"EP-{type_code}-{str(uuid.uuid4())[:8].upper()}"
        super().save(*args, **kwargs)
    

    class Meta:
        ordering = ['sort_order', 'name']
        indexes = [
            models.Index(fields=['product_type', 'is_active']),
            models.Index(fields=['featured', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_product_type_display()})"
    
    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})

class DigitalProduct(models.Model):
    """
    Digital game editions and downloadable content.
    Extends Product for base_game types with platform and edition info.
    """
    PC = 'pc'
    XBOX = 'xbox'
    NINTENDO = 'nintendo'
    
    PLATFORM_CHOICES = [
        (PC, 'PC (Steam/Epic)'),
        (XBOX, 'Xbox'),
        (NINTENDO, 'Nintendo Switch'),
    ]
    
    STANDARD = 'standard'
    PREMIUM = 'premium'
    ULTIMATE = 'ultimate'
    
    EDITION_CHOICES = [
        (STANDARD, 'Standard Edition'),
        (PREMIUM, 'Premium Edition'),
        (ULTIMATE, 'Ultimate Edition'),
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='digital')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    edition = models.CharField(max_length=20, choices=EDITION_CHOICES)
    requires_key = models.BooleanField(default=True)  

    class Meta:
        unique_together = ['platform', 'edition']  # Only one Standard PC edition, etc.
    
    def __str__(self):
        return f"{self.product.name} - {self.get_platform_display()} {self.get_edition_display()}"


class CurrencyProduct(models.Model):
    """
    In-game currency packs for purchase.
    Extends Product for currency types with credit amounts.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='currency')
    credit_amount = models.IntegerField()  # Amount of in-game credits
    
    def __str__(self):
        return f"{self.credit_amount:,} Credits"

class Wishlist(models.Model):
    """
    User wishlist for saving products for later purchase.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'product']  # Prevent duplicate wishlist entries
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    

# Auto-create related product extensions upon product creation
@receiver(post_save, sender=Product)
def create_product_extension(sender, instance, created, **kwargs):
    """Auto-create product extension based on type when a new Product is saved.
    
    This prevents the 'fiddly' admin workflow where users had to manually
    create and link extension records. Now when you create a Product:
    
    1. Product is saved with product_type
    2. Signal automatically creates the appropriate extension (DigitalProduct, 
       CurrencyProduct) with default of 0 values
    3. Admin can then edit the extension details via inlines or separate admin
    
    Example: Create Product with product_type='currency' 
    → CurrencyProduct is auto-created with credit_amount= 0
    → Admin edits to set actual credit amount (e.g., 500, 1000)
    """
    if created: # Only run on creation, not updates
        if instance.product_type == Product.CURRENCY:
            CurrencyProduct.objects.get_or_create(product=instance, defaults={'credit_amount': 0})
        elif instance.product_type == Product.BASE_GAME:
            DigitalProduct.objects.get_or_create(
                product=instance, 
                defaults={'platform': 'pc', 'edition': 'standard', 'requires_key': True}
            )
        