from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list(request):
    """Simple product list view for development testing."""
    products = Product.objects.filter(is_active=True)
    return render(request, 'catalog/product_list.html', {'products': products})