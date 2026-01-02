from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Product


# Create your views here.
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


@ensure_csrf_cookie
def edition_detail(request, product_slug, platform=None, edition=None):
    """
    display base game edition selection page with platform and edition variants
    
    supports url patterns:
    - /products/base-game/eclipse-protocol/  (shows default variant)
    - /products/base-game/eclipse-protocol/pc/standard/  (shows specific variant)
    """
    # get the base game product
    base_product = get_object_or_404(
        Product,
        slug=product_slug,
        product_type='base_game',
        is_active=True
    )
    
    # get all active variants for this product
    variants = base_product.digital_variants.filter(is_active=True).order_by('sort_order', 'platform', 'edition')
    
    # determine which variant to display
    selected_variant = None
    if platform and edition:
        # specific variant requested via url
        try:
            selected_variant = variants.get(platform=platform, edition=edition)
        except:
            pass
    
    # if no variant selected or url variant not found, use first available
    if not selected_variant and variants.exists():
        selected_variant = variants.first()
    
    # organize variants by platform for easy template rendering
    variants_by_platform = {}
    for variant in variants:
        if variant.platform not in variants_by_platform:
            variants_by_platform[variant.platform] = []
        variants_by_platform[variant.platform].append(variant)
    
    # get unique platforms preserving sort_order set by admin interface
    platforms = []
    for variant in variants:
        if variant.platform not in platforms:
            platforms.append(variant.platform)
    
    # get unique editions preserving desired order (standard, premium, ultimate)
    edition_order = ['standard', 'premium', 'ultimate']
    editions = []
    for edition in edition_order:
        if any(v.edition == edition for v in variants):
            editions.append(edition)
    
    # playstation store link (for modal)
    playstation_store_url = "https://store.playstation.com/"  
    
    context = {
        'base_product': base_product,
        'selected_variant': selected_variant,
        'variants': variants,
        'variants_by_platform': variants_by_platform,
        'platforms': platforms,
        'editions': editions,
        'playstation_store_url': playstation_store_url,
    }
    
    return render(request, 'catalog/edition_detail.html', context)

def search_results(request):
    """
    Search products by name and description.
    Returns both base games and currency products that match the query.
    """
    query = request.GET.get('q', '').strip()
    
    context = {
        'query': query,
        'products': [],
        'total_count': 0,
    }
    
    if query:
        # Search in product names and descriptions
        search_filter = (
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        
        # Get all matching active products
        products = Product.objects.filter(
            search_filter,
            is_active=True
        ).select_related('currency').prefetch_related('digital_variants')
        
        context['products'] = products
        context['total_count'] = products.count()
    
    return render(request, 'catalog/search_results.html', context)