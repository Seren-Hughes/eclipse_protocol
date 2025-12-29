from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
import uuid


class Product(models.Model):
    """
    Core product model representing all sellable items in the Eclipse Protocol store.
    
    Acts as the base for all product types:
    - BASE_GAME: Games with platform/edition variants (uses DigitalVariant)
    - DIGITAL: Simple digital products like DLC (uses DigitalProduct extension)
    - CURRENCY: In-game credit packs (uses CurrencyProduct extension)
    
    Design pattern: This follows the "product with variants" e-commerce pattern
    where the Product is the catalog item and variants are the purchasable options.
    """
    
    # Product type constants - defines how the product is structured
    BASE_GAME = 'base_game'  # Main games with platform/edition selection
    CURRENCY = 'currency'    # Credit packs with fixed amounts
    DIGITAL = 'digital'      # Simple digital products (DLC, expansions)
    
    PRODUCT_TYPE_CHOICES = [
        (BASE_GAME, 'Base Game'),
        (DIGITAL, 'Digital Product'),
        (CURRENCY, 'In-Game Currency'),
    ]

    # Core product information
    name = models.CharField(max_length=255, help_text="Product display name")
    slug = models.SlugField(max_length=255, unique=True, help_text="URL-friendly identifier")
    sku = models.CharField(
        max_length=50, 
        blank=True, 
        unique=True,
        help_text="Stock Keeping Unit - auto-generated if empty"
    )
    description = models.TextField(help_text="Main product description (shared across variants)")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Base price - variants can override this"
    )
    product_type = models.CharField(
        max_length=20, 
        choices=PRODUCT_TYPE_CHOICES,
        help_text="Determines which extension model is used"
    )
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True,
        help_text="Main product image (variants can have their own)"
    )

    # Catalog management
    is_active = models.BooleanField(default=True, help_text="Show in catalog")
    featured = models.BooleanField(default=False, help_text="Highlight on homepage")
    sort_order = models.IntegerField(default=0, help_text="Manual ordering within category")
    
    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Auto-generate SKU using product type prefix and UUID"""
        if not self.sku:
            type_codes = {
                'base_game': 'BG',
                'currency': 'CR', 
                'digital': 'DG',
            }
            type_code = type_codes.get(self.product_type, 'XX')
            self.sku = f"EP-{type_code}-{str(uuid.uuid4())[:8].upper()}"
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "All Products"
        ordering = ['sort_order', 'name']
        indexes = [
            models.Index(fields=['product_type', 'is_active']),  # Catalog filtering
            models.Index(fields=['featured', '-created_at']),    # Homepage queries
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_product_type_display()})"
    
    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})


class DigitalProduct(models.Model):
    """
    Extension for simple digital products that don't need variants.
    
    Used for DLC, expansions, standalone digital content where there's
    only one version per platform. For games with multiple platform/edition
    combinations, use DigitalVariant instead.
    
    OneToOne relationship ensures each Product has at most one DigitalProduct.
    """
    
    # Platform constants - kept here for reference by DigitalVariant
    PC = 'pc'
    XBOX = 'xbox'
    NINTENDO = 'nintendo'
    
    PLATFORM_CHOICES = [
        (PC, 'PC (Steam/Epic)'),
        (XBOX, 'Xbox'),
        (NINTENDO, 'Nintendo Switch'),
    ]
    
    # Edition constants - defines content/pricing tiers
    STANDARD = 'standard'
    PREMIUM = 'premium'
    ULTIMATE = 'ultimate'
    
    EDITION_CHOICES = [
        (STANDARD, 'Standard Edition'),
        (PREMIUM, 'Premium Edition'),
        (ULTIMATE, 'Ultimate Edition'),
    ]

    product = models.OneToOneField(
        Product, 
        on_delete=models.CASCADE, 
        related_name='digital',
        help_text="Parent product this extends"
    )
    platform = models.CharField(
        max_length=20, 
        choices=PLATFORM_CHOICES, 
        null=True, 
        blank=True,
        help_text="Target platform (optional for multi-platform)"
    )
    edition = models.CharField(
        max_length=20, 
        choices=EDITION_CHOICES, 
        null=True, 
        blank=True,
        help_text="Content edition level (optional)"
    )
    requires_key = models.BooleanField(
        default=True,
        help_text="Whether this product needs a game key for activation"
    )
    
    def __str__(self):
        platform_str = self.get_platform_display() or "Multi-Platform"
        edition_str = self.get_edition_display() or "Standard"
        return f"{self.product.name} - {platform_str} {edition_str}"


class CurrencyProduct(models.Model):
    """
    Extension for in-game currency products.
    
    Represents credit packs that players can purchase to spend within
    the game. Each currency product has a specific credit amount.
    
    Design note: Using separate products per tier (100, 200, 500 credits)
    rather than variants because each tier is effectively a different product
    with different pricing and a simple selection in the store.
    """
    
    product = models.OneToOneField(
        Product, 
        on_delete=models.CASCADE, 
        related_name='currency',
        help_text="Parent product this extends"
    )
    credit_amount = models.IntegerField(
        help_text="Number of in-game credits this purchase provides"
    )
    
    def __str__(self):
        return f"{self.credit_amount:,} Credits"


class DigitalVariant(models.Model):
    """
    Platform and edition variants for base game products.
    
    Allows a single base game Product to have multiple purchasable versions:
    - Different platforms (PC, Xbox, Nintendo)
    - Different editions (Standard, Premium, Ultimate)
    - Different pricing per combination
    - Platform-specific images and descriptions
    
    This follows the standard e-commerce variant pattern where the parent Product
    is the catalog item and variants are the actual purchasable SKUs.
    
    Example: "Eclipse Protocol" base game might have:
    - PC Standard (£19.99)
    - PC Ultimate (£39.99)  
    - Xbox Standard (£24.99)
    - etc.
    """
    
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='digital_variants',
        help_text="Base game this variant belongs to"
    )
    platform = models.CharField(
        max_length=20, 
        choices=DigitalProduct.PLATFORM_CHOICES,
        help_text="Gaming platform for this variant"
    )
    edition = models.CharField(
        max_length=20, 
        choices=DigitalProduct.EDITION_CHOICES,
        help_text="Content edition level"
    )
    requires_key = models.BooleanField(
        default=True,
        help_text="Whether this variant needs a game key"
    )
    price_override = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        help_text="Optional: Override base product price for this variant"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this variant is available for purchase"
    )
    sort_order = models.IntegerField(
        default=0,
        help_text="Display order within the product's variants"
    )
    sku = models.CharField(
        max_length=64, 
        blank=True, 
        null=True,
        help_text="Unique identifier - auto-generated from base product SKU"
    )
    description = models.TextField(
        blank=True, 
        help_text="Edition-specific features (e.g., 'Includes season pass, exclusive skins')"
    )
    image = models.ImageField(
        upload_to='variants/', 
        blank=True, 
        null=True, 
        help_text="Edition-specific image (falls back to product image if empty)"
    )

    class Meta:
        unique_together = [('product', 'platform', 'edition')]
        ordering = ['sort_order', 'platform', 'edition']
        verbose_name = "Base Game Variant"
        verbose_name_plural = "Base Game Variants"

    @property
    def full_description(self):
        """
        Combine base product description with variant-specific details.
        Used on product pages to show complete information for this variant.
        """
        base_desc = self.product.description
        if self.description:
            edition_name = self.get_edition_display().replace(' Edition', '')  
            return f"{base_desc}\n\n**{edition_name} Edition Includes:**\n{self.description}"
        return base_desc
    
    @property
    def effective_image(self):
        """
        Return variant image if available, otherwise fall back to product image.
        Ensures every variant has an image for display purposes.
        """
        return self.image if self.image else self.product.image

    @property
    def effective_price(self):
        """
        Return variant-specific price or fall back to base product price.
        Allows per-variant pricing (e.g., premium editions cost more).
        """
        return self.price_override if self.price_override is not None else self.product.price

    def save(self, *args, **kwargs):
        """Auto-generate variant SKU from base product SKU + platform + edition"""
        if not self.sku or not self.sku.strip():
            base = self.product.sku or f"EP-{self.product_id}"
            plat = self.platform.upper()
            ed = self.edition.upper()
            candidate = f"{base}-{plat}-{ed}"
            
            # Ensure uniqueness by adding number suffix if needed
            sku = candidate
            i = 1
            while DigitalVariant.objects.filter(sku=sku).exclude(pk=self.pk).exists():
                i += 1
                sku = f"{candidate}-{i}"
            self.sku = sku
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} / {self.get_platform_display()} / {self.get_edition_display()}"


class Wishlist(models.Model):
    """
    User wishlist functionality for saving products for later purchase.
    
    Allows users to bookmark products they're interested in but not ready
    to buy immediately. Useful for sales notifications and purchase reminders.
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='wishlists',
        help_text="User who wishlisted the product"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        help_text="Product added to wishlist"
    )
    variant = models.ForeignKey(
        'DigitalVariant',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Specific variant (platform/edition) if applicable"
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When product was added to wishlist"
    )
    
    class Meta:
        constraints = [
            # Ensure unique wishlist entries per user/product/variant combination
            models.UniqueConstraint(
                fields=['user', 'product', 'variant'],
                name='uniq_wishlist_user_product_variant'
            ),
            # Ensure unique wishlist entries per user/product when variant is null
            models.UniqueConstraint(
                fields=['user', 'product'],
                condition=Q(variant__isnull=True),
                name='uniq_wishlist_user_product_null_variant'
            ),
        ]
        ordering = ['-added_at']  # Show most recent first
    
    def __str__(self):
        if self.variant:
            return f"{self.user.username} - {self.product.name} ({self.variant.get_platform_display()} - {self.variant.get_edition_display()})"
        return f"{self.user.username} - {self.product.name}"
    

@receiver(post_save, sender=Product)
def create_product_extension(sender, instance, created, **kwargs):
    """
    Auto-create appropriate extension models when a Product is created.
    
    - CURRENCY products get a CurrencyProduct extension (with 0 credits initially)
    - DIGITAL products get a DigitalProduct extension  
    - BASE_GAME products use only DigitalVariant (no auto-created extension)
    
    This ensures the proper data structure is set up based on product type
    without requiring manual admin steps.
    """
    if created:
        if instance.product_type == Product.CURRENCY:
            CurrencyProduct.objects.get_or_create(
                product=instance, 
                defaults={'credit_amount': 0}
            )
        elif instance.product_type == Product.DIGITAL:
            DigitalProduct.objects.get_or_create(product=instance)
