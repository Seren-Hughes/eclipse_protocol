from datetime import datetime, timedelta

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Count, Sum
from django.shortcuts import render

from catalog.models import Product
from checkout.models import Order


# Create your views here.
def home(request):
    # Get featured currency packs for bestsellers section
    featured_currency_packs = Product.objects.filter(
        product_type='currency',
        is_active=True,
        featured=True
    ).order_by('price')[:6]  # Order by price, limit to 6
    
    context = {
        'featured_currency_packs': featured_currency_packs,
    }
    return render(request, "core/home.html", context)


@staff_member_required
def admin_sales_dashboard(request):
    """
    Simple admin-only sales dashboard showing key metrics
    Only accessible to Django admin users (staff)
    """
    # Basic sales metrics
    total_orders = Order.objects.filter(payment_status='paid').count()
    total_revenue = Order.objects.filter(payment_status='paid').aggregate(
        total=Sum('total_amount')
    )['total'] or 0
    
    average_order_value = Order.objects.filter(payment_status='paid').aggregate(
        avg=Avg('total_amount')
    )['avg'] or 0
    
    # Recent orders (last 30 days)
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_orders = Order.objects.filter(
        payment_status='paid',
        order_date__gte=thirty_days_ago
    ).count()
    
    recent_revenue = Order.objects.filter(
        payment_status='paid',
        order_date__gte=thirty_days_ago
    ).aggregate(total=Sum('total_amount'))['total'] or 0
    
    # Latest 10 orders for quick reference
    latest_orders = Order.objects.filter(
        payment_status='paid'
    ).order_by('-order_date')[:10]
    
    context = {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'average_order_value': round(average_order_value, 2) if average_order_value else 0,
        'recent_orders_count': recent_orders,
        'recent_revenue': recent_revenue,
        'latest_orders': latest_orders,
    }
    
    return render(request, 'admin/sales_dashboard.html', context)