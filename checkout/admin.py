from django.contrib import admin
from .models import Order, OrderItem, Payment, LicenseKey

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


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Payment administration interface"""
    
    list_display = ('transaction_id', 'order', 'amount', 'status', 'payment_date')
    list_filter = ('status', 'payment_date')
    search_fields = ('transaction_id', 'order__order_number', 'stripe_charge_id')
    readonly_fields = ('payment_date', 'is_successful')
    
    fieldsets = (
        ('Payment Information', {
            'fields': ('order', 'transaction_id', 'amount')
        }),
        ('Status', {
            'fields': ('status', 'is_successful', 'payment_date')
        }),
        ('Stripe Details', {
            'fields': ('stripe_charge_id', 'failure_reason'),
            'classes': ('collapse',)
        })
    )

    def is_successful(self, obj):
            return obj.is_successful
    is_successful.boolean = True
    is_successful.short_description = 'Successful'

@admin.register(LicenseKey)
class LicenseKeyAdmin(admin.ModelAdmin):
    """License key administration interface"""
    
    list_display = ('key_code', 'user', 'product_name', 'platform', 'status', 'email_sent', 'created_at')
    list_filter = ('platform', 'status', 'email_sent', 'created_at')
    search_fields = ('key_code', 'user__username', 'user__email', 'product__name')
    readonly_fields = ('created_at', 'email_sent_at', 'last_downloaded', 'download_count')
    
    fieldsets = (
        ('Key Information', {
            'fields': ('key_code', 'platform', 'status')
        }),
        ('Ownership', {
            'fields': ('user', 'order_item', 'product', 'variant')
        }),
        ('Delivery Status', {
            'fields': ('email_sent', 'email_sent_at', 'download_count', 'last_downloaded')
        }),
        ('Lifecycle', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    actions = ['mark_as_sent', 'revoke_keys']

    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Product'
    product_name.admin_order_field = 'product__name'
    
    def mark_as_sent(self, request, queryset):
        """Mark selected keys as sent"""
        count = 0
        for key in queryset:
            if not key.email_sent:
                key.mark_as_sent()
                count += 1
        
        self.message_user(request, f'{count} license keys marked as sent.')
    mark_as_sent.short_description = 'Mark selected keys as sent'
    
    def revoke_keys(self, request, queryset):
        """Revoke selected keys"""
        count = queryset.update(status=LicenseKey.KEY_REVOKED)
        self.message_user(request, f'{count} license keys revoked.')
    revoke_keys.short_description = 'Revoke selected keys'