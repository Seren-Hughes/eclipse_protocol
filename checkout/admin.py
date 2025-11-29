from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    """Inline display of order items"""
    model = OrderItem
    readonly_fields = ('total_price', 'created_at')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order administration interface"""
    
    list_display = (
        'order_number', 'user', 'full_name', 'email', 
        'total_amount', 'payment_status', 'delivery_status', 'order_date'
    )
    list_filter = ('payment_status', 'delivery_status', 'order_date')
    search_fields = ('order_number', 'email', 'full_name')
    readonly_fields = ('order_number', 'order_date', 'item_count')
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'order_date', 'total_amount')
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
        ('Summary', {
            'fields': ('item_count',),
            'classes': ('collapse',)
        })
    )
    
    inlines = [OrderItemInline]
    
    def item_count(self, obj):
        return obj.item_count
    item_count.short_description = 'Total Items'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Direct order item administration"""
    
    list_display = ('order', 'product_name', 'variant_details', 'quantity', 'unit_price', 'total_price')
    list_filter = ('created_at', 'product__product_type')
    search_fields = ('order__order_number', 'product_name')
    readonly_fields = ('total_price', 'created_at')