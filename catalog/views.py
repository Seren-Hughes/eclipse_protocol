from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    """Simple product list view for development testing."""
    products = Product.objects.filter(is_active=True)
    return render(request, 'catalog/product_list.html', {'products': products})

def currency_detail(request, product_slug=None):
    """Display currency selection page with all available credit packs"""
    # Get all active currency products
    currency_products = Product.objects.filter(
        product_type='currency', 
        is_active=True
    ).select_related('currency').order_by('price')
    
    # Default page info with default image
    page_info = {
        'name': 'Eclipse Protocol Credits',
        'description': 'In-game currency for Eclipse Protocol',
        'image': None  # image added via first product
    }
    
    # Set default image from the first currency product if available
    if currency_products.exists():
        # use the first currency product's image as default
        first_product = currency_products.first()
        if first_product.image:
            page_info['image'] = first_product.image
    
    # If a specific product slug is provided, get that product's image/info
    selected_product = None
    if product_slug:
        try:
            selected_product = Product.objects.get(
                slug=product_slug, 
                product_type='currency',
                is_active=True
            )
            page_info = {
                'name': selected_product.name,
                'description': selected_product.description,
                'image': selected_product.image
            }
        except Product.DoesNotExist:
            pass  # Use default page_info
    
    context = {
        'page_info': page_info,
        'currency_products': currency_products,
        'selected_product': selected_product,
    }
    return render(request, 'catalog/currency_detail.html', context)