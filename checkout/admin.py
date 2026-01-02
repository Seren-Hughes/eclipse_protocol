from django.contrib import admin

from .models import LicenseKey, Order, OrderItem, Payment

# Register your models here.

class OrderItemInline(admin.TabularInline):
    """Inline display of order items"""
    model = OrderItem
    readonly_fields = ('total_price', 'created_at')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order administration interface"""
    
    readonly_fields = ('order_number', 'order_date', 'item_count', 'original_cart')
    
    list_display = ('order_number', 'order_date', 'full_name', 'total_amount', 
                    'payment_status', 'delivery_status')
    
    list_filter = ('payment_status', 'delivery_status', 'order_date')
    search_fields = ('order_number', 'email', 'full_name')
    ordering = ('-order_date',)
    
    # Remove the duplicate fields definition and keep only fieldsets
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'order_date', 'total_amount', 'stripe_pid')
        }),
        ('Status', {
            'fields': ('payment_status', 'delivery_status', 'subscription_renewal')
        }),
        ('Customer Details', {
            'fields': ('full_name', 'email', 'phone_number')
        }),
        ('Address', {
            'fields': ('street_address_1', 'street_address_2', 'city', 'postcode', 'country')
        }),
        ('Cart Details', {
            'fields': ('original_cart',),
            'classes': ('collapse',)
        }),
        ('Summary', {
            'fields': ('item_count',),
            'classes': ('collapse',)
        })
    )
    
    inlines = [OrderItemInline]
    
    def item_count(self, obj):
        """Display number of items in order"""
        return obj.items.count()
    item_count.short_description = 'Number of Items'