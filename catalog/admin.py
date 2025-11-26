from django.contrib import admin
from .models import Product, DigitalProduct, CurrencyProduct

# Register your models here.

# Inline admin classes for product extensions
class DigitalProductInline(admin.StackedInline):
    """Display digital product details inline with the main product"""
    model = DigitalProduct
    extra = 0

    def get_queryset(self, request):
        """
        Only show digital products for base_game product types.
        
        Note: This prevents confusion in admin by filtering the inline
        to only show relevant digital products, not all non-physical products.
        """
        qs = super().get_queryset(request)
        return qs.filter(product__product_type='base_game')

class CurrencyProductInline(admin.StackedInline):
    """Display currency product details inline with the main product"""
    model = CurrencyProduct
    extra = 0



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Main product admin with inline extensions for different product types.
    Provides filtering, search, and bulk actions for product management.
    """
    list_display = ('name', 'sku', 'product_type', 'image_preview', 'display_price', 'is_active', 'featured', 'created_at')
    list_filter = ('product_type', 'is_active', 'featured', 'created_at')
    search_fields = ('name', 'description', 'sku')
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from name
    ordering = ('sort_order', 'name')
    
    # Show appropriate inline based on product type
    inlines = [DigitalProductInline, CurrencyProductInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'sku', 'description', 'image', 'price', 'product_type')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'featured', 'sort_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        """Save product and check for incomplete product extensions"""
        super().save_model(request, obj, form, change)
    
        # Check for incomplete currency products after save
        if obj.product_type == Product.CURRENCY:
            if hasattr(obj, 'currency') and obj.currency.credit_amount == 0:
                from django.contrib import messages
                messages.warning(request, 
                    f"Remember to set the credit amount for '{obj.name}' in the Currency Product section below!")

        elif obj.product_type == Product.BASE_GAME:
            if hasattr(obj, 'digital'):
                # Check if still using defaults
                digital = obj.digital
                if digital.platform == 'pc' and digital.edition == 'standard':
                    messages.info(request,
                        f"Verify platform and edition settings for '{obj.name}' in the Digital Product section below!")
    
    # Bulk actions
    actions = ['make_active', 'make_inactive', 'make_featured']
    
    def make_active(self, request, queryset):
        """Bulk action to activate selected products"""
        queryset.update(is_active=True)
        self.message_user(request, f'{queryset.count()} products activated.')
    make_active.short_description = "Mark selected products as active"
    
    def make_inactive(self, request, queryset):
        """Bulk action to deactivate selected products"""
        queryset.update(is_active=False)
        self.message_user(request, f'{queryset.count()} products deactivated.')
    make_inactive.short_description = "Mark selected products as inactive"
    
    def make_featured(self, request, queryset):
        """Bulk action to feature selected products"""
        queryset.update(featured=True)
        self.message_user(request, f'{queryset.count()} products featured.')
    make_featured.short_description = "Mark selected products as featured"

    def display_price(self, obj):
        """Display UK price (base market)"""
        return f"£{obj.price}"  
    display_price.short_description = 'UK Price'
    display_price.admin_order_field = 'price'  # Allow sorting

    def image_preview(self, obj):
        """Display small preview of product image in admin list"""
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="max-height:50px;">', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(DigitalProduct)
class DigitalProductAdmin(admin.ModelAdmin):
    """
    Admin for digital products with platform and edition filtering.
    """
    list_display = ('product', 'platform', 'edition', 'requires_key')
    list_filter = ('platform', 'edition', 'requires_key')
    search_fields = ('product__name',)
    ordering = ('platform', 'edition')

    def delete_model(self, request, obj):
        """
        Delete the base product when extension is deleted.
        Prevents orphaned base products without extensions.
        """
        product = obj.product
        super().delete_model(request, obj)
        product.delete()
    
    def delete_queryset(self, request, queryset):
        """Handle bulk deletes"""
        products = [obj.product for obj in queryset]
        super().delete_queryset(request, queryset)
        for product in products:
            product.delete()


@admin.register(CurrencyProduct)
class CurrencyProductAdmin(admin.ModelAdmin):
    """
    Admin for currency products showing credit amounts.
    """
    list_display = ('product', 'credit_amount')
    search_fields = ('product__name',)
    ordering = ('credit_amount',)

    def delete_model(self, request, obj):
        """Delete the base product when currency product is deleted"""
        product = obj.product
        super().delete_model(request, obj)
        product.delete()
    
    def delete_queryset(self, request, queryset):
        """Handle bulk deletes"""
        products = [obj.product for obj in queryset]
        super().delete_queryset(request, queryset)
        for product in products:
            product.delete()


        