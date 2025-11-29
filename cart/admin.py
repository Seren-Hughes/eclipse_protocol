from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartItemInline(admin.TabularInline):
    """
    Inline admin interface for cart items within a cart.
    Allows quick viewing and editing of items in a user's cart.
    """
    model = CartItem
    extra = 0
    readonly_fields = ('added_at', 'line_total_display', 'effective_price_display')
    fields = ('product', 'variant', 'quantity', 'effective_price_display', 'line_total_display', 'added_at')
    
    @admin.display(description='Line Total')
    def line_total_display(self, obj):
        return f"£{obj.line_total:.2f}"
    
    @admin.display(description='Unit Price')
    def effective_price_display(self, obj):
        return f"£{obj.effective_price:.2f}"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Admin interface for user carts.
    Useful for customer support and abandoned cart analysis.
    """
    list_display = ('user', 'total_items', 'total_price', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at', 'total_items', 'total_price')
    inlines = [CartItemInline]
    
    def total_price(self, obj):
        return f"£{obj.total_price:.2f}"
    total_price.short_description = 'Cart Total'
    total_price.admin_order_field = 'updated_at'  # Sortable column


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Direct admin interface for cart items.
    Useful for troubleshooting cart issues.
    """
    list_display = ('cart_user', 'product', 'variant', 'quantity', 'line_total_display', 'added_at')
    list_filter = ('added_at', 'product__product_type')
    search_fields = ('cart__user__username', 'product__name')
    raw_id_fields = ('cart', 'product', 'variant')
    
    def cart_user(self, obj):
        return obj.cart.user.username
    cart_user.short_description = 'User'
    cart_user.admin_order_field = 'cart__user__username'
    
    def line_total_display(self, obj):
        return f"£{obj.line_total:.2f}"
    line_total_display.short_description = 'Line Total'