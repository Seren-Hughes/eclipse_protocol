from django import forms
from django.contrib import admin, messages
from django.db.models import Count

from .models import CurrencyProduct, DigitalProduct, DigitalVariant, Product

# ===== INLINE ADMIN CLASSES =====


class DigitalProductInline(admin.StackedInline):
    """
    Inline admin for simple digital products (DLC, expansions).

    Only shown for DIGITAL product type. Provides platform/edition
    configuration for digital products that don't need variants.
    """

    model = DigitalProduct
    extra = 0

    def get_queryset(self, request):
        """
        Filter to only show digital products for base_game product types.

        Prevents admin confusion by showing only relevant digital products.
        Note: This filter may need adjustment based on product type logic.
        """
        qs = super().get_queryset(request)
        return qs.filter(product__product_type="base_game")


class CurrencyProductInline(admin.StackedInline):
    """
    Inline admin for currency products (in-game credit packs).

    Only shown for CURRENCY product type. Allows setting the credit
    amount that this product provides to players.
    """

    model = CurrencyProduct
    extra = 0


class DigitalVariantInline(admin.TabularInline):
    """
    Inline admin for base game platform/edition variants.

    Uses tabular layout since base games typically have multiple variants.
    Each variant represents a unique purchasable SKU with platform/edition
    combination and optional price override.
    """

    model = DigitalVariant
    extra = 1
    fields = (
        "platform",
        "edition",
        "image",
        "description",
        "sku",
        "price_override",
        "requires_key",
        "is_active",
        "sort_order",
    )
    readonly_fields = ("sku",)  # SKU auto-generated on save
    ordering = ("sort_order", "platform", "edition")


# ===== ADMIN FORMS =====


class ProductAdminForm(forms.ModelForm):
    """
    Custom form validation for Product creation/editing.

    Ensures base game products have valid pricing since variants
    depend on the base price for effective price calculations.
    """

    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        """Validate that base game products have a positive base price"""
        price = self.cleaned_data.get("price")
        product_type = self.cleaned_data.get("product_type")

        if product_type == Product.BASE_GAME and (not price or price <= 0):
            raise forms.ValidationError(
                "Base game products must have a valid base price for variant pricing calculations."
            )
        return price


# ===== MAIN ADMIN CLASSES =====


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Main product administration interface for all product types.

    Features:
    - Dynamic inline selection based on product type
    - Variant count display for base games
    - Price validation for base games
    - Bulk actions for common operations
    - Auto-slug generation from product name
    - Post-save validation with helpful messages

    Product Types:
    - BASE_GAME: Uses DigitalVariant for platform/edition selection
    - DIGITAL: Uses DigitalProduct for simple digital items (DLC)
    - CURRENCY: Uses CurrencyProduct for credit pack configuration
    """

    form = ProductAdminForm

    # List view configuration
    list_display = (
        "name",
        "sku",
        "product_type",
        "image_preview",
        "display_price",
        "variant_count",
        "is_active",
        "featured",
    )
    list_filter = ("product_type", "is_active", "featured")
    search_fields = ("name", "sku")
    prepopulated_fields = {
        "slug": ("name",)
    }  # Auto-generate URL-friendly slug
    ordering = ("product_type", "name")

    def get_queryset(self, request):
        """Add variant count annotation for efficient list display"""
        return (
            super()
            .get_queryset(request)
            .annotate(_variant_count=Count("digital_variants"))
        )

    @admin.display(ordering="_variant_count", description="Variants")
    def variant_count(self, obj):
        """Show variant count for base games, dash for other types"""
        count = getattr(obj, "_variant_count", 0)
        if obj.product_type == Product.BASE_GAME:
            return f"{count} variants"
        return "-"

    def display_price(self, obj):
        """Display formatted base price in GBP (primary market)"""
        return f"£{obj.price}"

    display_price.short_description = "UK Price"
    display_price.admin_order_field = "price"  # Enable column sorting

    def image_preview(self, obj):
        """Display thumbnail preview of product image in list view"""
        if obj.image:
            from django.utils.html import format_html

            return format_html(
                '<img src="{}" style="max-height:50px; max-width:50px;">',
                obj.image.url,
            )
        return "No image"

    image_preview.short_description = "Preview"

    # Form layout organization
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "sku",
                    "description",
                    "image",
                    "price",
                    "product_type",
                )
            },
        ),
        (
            "Display Settings",
            {"fields": ("is_active", "featured", "sort_order")},
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),  # Start collapsed to reduce clutter
            },
        ),
    )

    readonly_fields = ("created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        """
        Save product and validate configuration completeness.

        Provides helpful admin messages to guide proper product setup:
        - Currency products: Check credit amount is set
        - Base games: Check variants exist and are active
        - Digital products: Check platform/edition configuration
        """
        super().save_model(request, obj, form, change)

        if not change:  # Only check new products after they're created
            obj.refresh_from_db()

        # Validate product configuration based on type
        if obj.product_type == Product.CURRENCY:
            self._validate_currency_product(request, obj)
        elif obj.product_type == Product.BASE_GAME:
            self._validate_base_game_product(request, obj)
        elif obj.product_type == Product.DIGITAL:
            self._validate_digital_product(request, obj)

    def _validate_currency_product(self, request, obj):
        """Check currency product has proper credit amount configured"""
        try:
            currency = obj.currency
            if currency.credit_amount == 0:
                self.message_user(
                    request,
                    f"Set credit amount for '{obj.name}' in Currency Product section.",
                    level=messages.WARNING,
                )
        except CurrencyProduct.DoesNotExist:
            self.message_user(
                request,
                f"Currency extension missing for '{obj.name}'. Check the signal is working.",
                level=messages.ERROR,
            )

    def _validate_base_game_product(self, request, obj):
        """Check base game has platform/edition variants configured"""
        variant_count = obj.digital_variants.count()
        if variant_count == 0:
            self.message_user(
                request,
                f"Add platform/edition variants for '{obj.name}' in Base Game Variants section.",
                level=messages.WARNING,
            )
        else:
            active_variants = obj.digital_variants.filter(
                is_active=True
            ).count()
            if active_variants == 0:
                self.message_user(
                    request,
                    f"No active variants for '{obj.name}'. Enable at least one variant to sell this product.",
                    level=messages.WARNING,
                )

    def _validate_digital_product(self, request, obj):
        """Check digital product has platform/edition settings configured"""
        digital = getattr(obj, "digital", None)
        if not digital:
            self.message_user(
                request,
                f"Digital extension missing for '{obj.name}'.",
                level=messages.ERROR,
            )
            return

        # Check for missing platform/edition configuration
        if not digital.platform or not digital.edition:
            self.message_user(
                request,
                f"Set platform and edition for '{obj.name}' in Digital Product section.",
                level=messages.WARNING,
            )

        # Remind about key requirements
        if digital.requires_key is False:
            self.message_user(
                request,
                f"Confirm if '{obj.name}' should require a key.",
                level=messages.INFO,
            )

    def get_inlines(self, request, obj=None):
        """
        Show appropriate inline admin based on product type.

        Returns the correct extension inline to avoid showing
        irrelevant configuration options for each product type.
        """
        if not obj:
            return []

        # Map product types to their appropriate inlines
        inline_map = {
            Product.BASE_GAME: [
                DigitalVariantInline
            ],  # Platform/edition variants
            Product.DIGITAL: [
                DigitalProductInline
            ],  # Simple digital product config
            Product.CURRENCY: [CurrencyProductInline],  # Credit amount setting
        }

        return inline_map.get(obj.product_type, [])

    # Bulk actions for efficient product management
    actions = ["make_active", "make_inactive", "make_featured"]

    def make_active(self, request, queryset):
        """Bulk activate selected products for sale"""
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} products activated.")

    make_active.short_description = "Mark selected products as active"

    def make_inactive(self, request, queryset):
        """Bulk deactivate selected products (remove from catalog)"""
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} products deactivated.")

    make_inactive.short_description = "Mark selected products as inactive"

    def make_featured(self, request, queryset):
        """Bulk feature selected products on homepage/promotional areas"""
        queryset.update(featured=True)
        self.message_user(request, f"{queryset.count()} products featured.")

    make_featured.short_description = "Mark selected products as featured"


@admin.register(DigitalVariant)
class DigitalVariantAdmin(admin.ModelAdmin):
    """
    Direct administration of base game platform/edition variants.

    Provides a dedicated interface for managing variants across all base games.
    Useful for:
    - Bulk variant operations (activate/deactivate)
    - Overview of all platform/edition combinations
    - Cross-product variant management
    - SKU and pricing oversight
    """

    list_display = (
        "product_name",
        "platform",
        "edition",
        "image_preview",
        "sku",
        "effective_price",
        "is_active",
        "sort_order",
    )
    list_filter = ("platform", "edition", "is_active", "product__product_type")
    search_fields = ("product__name", "sku")
    list_editable = ("is_active", "sort_order")
    ordering = ("product", "sort_order", "platform")
    raw_id_fields = ("product",)

    fieldsets = (
        ("Product Assignment", {"fields": ("product",)}),
        (
            "Variant Configuration",
            {
                "fields": (
                    "platform",
                    "edition",
                    "image",
                    "description",
                    "sku",
                    "requires_key",
                )
            },
        ),
        (
            "Pricing & Availability",
            {"fields": ("price_override", "is_active", "sort_order")},
        ),
    )

    readonly_fields = ("sku",)  # Auto-generated on save

    def get_queryset(self, request):
        """Optimize queries with product relationship"""
        return super().get_queryset(request).select_related("product")

    @admin.display(description="Product")
    def product_name(self, obj):
        """Display the base game this variant belongs to"""
        return obj.product.name

    @admin.display(description="Price")
    def effective_price(self, obj):
        """Display actual selling price (override or base product price)"""
        return f"£{obj.effective_price}"

    @admin.display(description="Image")
    def image_preview(self, obj):
        """Display variant-specific image or fallback to product image"""
        image = obj.effective_image  # Uses model's effective_image property
        if image:
            from django.utils.html import format_html

            return format_html(
                '<img src="{}" style="max-height:50px; max-width:50px;">',
                image.url,
            )
        return "No image"

    # Bulk actions for variant management
    actions = ["activate_variants", "deactivate_variants"]

    def activate_variants(self, request, queryset):
        """Bulk activate selected variants for purchase"""
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} variants activated.")

    activate_variants.short_description = "Activate selected variants"

    def deactivate_variants(self, request, queryset):
        """Bulk deactivate selected variants (remove from purchase options)"""
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} variants deactivated.")

    deactivate_variants.short_description = "Deactivate selected variants"


# ===== EXTENSION MODEL ADMINS =====
# Direct access to extension models for troubleshooting and advanced management


@admin.register(DigitalProduct)
class DigitalProductAdmin(admin.ModelAdmin):
    """
    Direct administration of simple digital products.

    For DLC, expansions, and other digital content that doesn't need
    platform/edition variants. Most management should be done through
    the main Product admin interface.
    """

    list_display = ("product", "platform", "edition", "requires_key")
    list_filter = ("platform", "edition", "requires_key")
    search_fields = ("product__name",)


@admin.register(CurrencyProduct)
class CurrencyProductAdmin(admin.ModelAdmin):
    """
    Direct administration of in-game currency products.

    Shows credit amounts alongside product pricing for quick comparison
    and credit pack pricing strategy management.
    """

    list_display = (
        "product",
        "credit_amount",
        "display_price",
        "image_preview",
        "is_active",
        "featured",
    )
    search_fields = ("product__name",)

    # Prevent creating products from Currency product panel - use main Product admin instead
    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        """Optimize queries with product relationship"""
        return super().get_queryset(request).select_related("product")

    def display_price(self, obj):
        """Display price from the related product"""
        return f"£{obj.product.price}"

    display_price.short_description = "Price"

    def image_preview(self, obj):
        """Display image preview from the related product"""
        if obj.product.image:
            from django.utils.html import format_html

            return format_html(
                '<img src="{}" style="max-height:50px; max-width:50px;">',
                obj.product.image.url,
            )
        return "No image"

    image_preview.short_description = "Preview"

    def is_active(self, obj):
        """Display active status from the related product"""
        return obj.product.is_active

    is_active.boolean = True  # Show as checkmark/X icon
    is_active.short_description = "Active"

    def featured(self, obj):
        """Display featured status from the related product"""
        return obj.product.featured

    featured.boolean = True  # Show as checkmark/X icon
    featured.short_description = "Featured"
