from django.shortcuts import render
from catalog.models import Product


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