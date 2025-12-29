from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Cart, CartItem
from catalog.models import Product, DigitalVariant
from decimal import Decimal
from .context_processors import cart_contents

def cart_view(request):
    """
    Display the shopping cart page.
    
    For authenticated users: Displays database cart items.
    For anonymous users: Displays session cart items via context processor.
    """
    if request.user.is_authenticated:
        # Get or create cart for authenticated user
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.select_related('product', 'variant', 'product__currency').all()
        total_price = cart.total_price
        total_items = cart.total_items
    else:
        # Use session cart for anonymous users
        cart_context = cart_contents(request)
        cart_items = cart_context['cart_items']
        total_price = cart_context['total']
        total_items = cart_context['product_count']
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_items': total_items,
        'shipping_cost': Decimal('0.00'),  # conditional shipping to be added for physical products (future scope)
        'grand_total': total_price,
    }
    
    return render(request, 'cart/cart.html', context)

@require_POST
def add_to_cart(request, product_id):
    """
    Add a product to the cart via AJAX.
    
    Supports both authenticated users (database cart) and anonymous users (session cart).
    Handles digital products with duplicate prevention and currency products with quantity increment.
    
    Args:
        product_id (int): ID of the product to add
        
    POST data:
        variant_id (optional): ID of the product variant
        quantity (optional): Quantity to add (defaults to 1)
        
    Returns:
        JsonResponse: Success/failure status with message and updated cart total
    """
    product = get_object_or_404(Product, id=product_id)
    variant_id = request.POST.get('variant_id')
    quantity = int(request.POST.get('quantity', 1))
    
    variant = None
    if variant_id:
        variant = get_object_or_404(DigitalVariant, id=variant_id, product=product)
    
    if request.user.is_authenticated:
        # Handle database cart for authenticated users
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Prevent duplicate digital products
        if product.product_type in [Product.BASE_GAME, Product.DIGITAL]:
            existing_item = CartItem.objects.filter(
                cart=cart,
                product=product,
                variant=variant
            ).first()
            
            if existing_item:
                item_name = product.name
                if variant:
                    item_name += f" ({variant.get_platform_display()} - {variant.get_edition_display()})"
                
                return JsonResponse({
                    'success': False,
                    'message': f'{item_name} is already in your cart'
                })
        
        # Get or create cart item
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            variant=variant,
            defaults={'quantity': quantity}
        )
        
        if not item_created:
            # For currency products, increment quantity
            if product.product_type == Product.CURRENCY:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # Digital products should not reach here due to check above
                item_name = product.name
                if variant:
                    item_name += f" ({variant.get_platform_display()} - {variant.get_edition_display()})"
                
                return JsonResponse({
                    'success': False,
                    'message': f'{item_name} is already in your cart'
                })
        
        cart_total = cart.total_items
    else:
        # Handle session cart for anonymous users
        session_cart = request.session.get('cart', {})
        
        # Create unique cart item key
        if variant:
            cart_key = f"{product_id}_{variant_id}"
        else:
            cart_key = str(product_id)
        
        # Prevent duplicate digital products
        if product.product_type in [Product.BASE_GAME, Product.DIGITAL]:
            if cart_key in session_cart:
                item_name = product.name
                if variant:
                    item_name += f" ({variant.get_platform_display()} - {variant.get_edition_display()})"
                
                return JsonResponse({
                    'success': False,
                    'message': f'{item_name} is already in your cart'
                })
        
        # Add or update item in session cart
        if cart_key in session_cart:
            # For currency products, increment quantity
            if product.product_type == Product.CURRENCY:
                session_cart[cart_key]['quantity'] += quantity
            else:
                # Digital products should not reach here due to check above
                item_name = product.name
                if variant:
                    item_name += f" ({variant.get_platform_display()} - {variant.get_edition_display()})"
                
                return JsonResponse({
                    'success': False,
                    'message': f'{item_name} is already in your cart'
                })
        else:
            # Create new cart item
            cart_item_data = {
                'product_id': product_id,
                'quantity': quantity,
            }
            if variant:
                cart_item_data['variant_id'] = variant_id
                cart_item_data['platform'] = variant.platform
            
            session_cart[cart_key] = cart_item_data
        
        request.session['cart'] = session_cart
        request.session.modified = True
        
        # Calculate total items in session cart
        cart_total = sum(item_data.get('quantity', 1) for item_data in session_cart.values())
    
    # Prepare response message
    item_name = product.name
    if variant:
        item_name += f" ({variant.get_platform_display()} - {variant.get_edition_display()})"
    
    return JsonResponse({
        'success': True,
        'message': f'{item_name} added to cart',
        'cart_total': cart_total
    })

@require_POST
def update_cart_item(request, item_id):
    """
    Update the quantity of a cart item via AJAX.
    
    Supports both authenticated users (database cart) and anonymous users (session cart).
    If quantity is 0, removes the item entirely.
    
    Args:
        item_id (str): For authenticated users: database CartItem ID
                      For anonymous users: session cart key (e.g., "22" or "22_15")
                      
    POST data:
        quantity (int): New quantity for the item
        
    Returns:
        JsonResponse: Success status with updated cart totals
    """
    quantity = int(request.POST.get('quantity', 1))
    
    if request.user.is_authenticated:
        # Handle database cart
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        
        return JsonResponse({
            'success': True,
            'cart_total': cart_item.cart.total_items,
            'cart_price': float(cart_item.cart.total_price)
        })
    else:
        # Handle session cart
        session_cart = request.session.get('cart', {})
        
        if item_id in session_cart:
            if quantity > 0:
                session_cart[item_id]['quantity'] = quantity
            else:
                del session_cart[item_id]
            
            request.session['cart'] = session_cart
            request.session.modified = True
            
            # Recalculate totals using context processor
            cart_total = sum(item_data.get('quantity', 1) for item_data in session_cart.values())
            cart_context_data = cart_contents(request)
            cart_price = cart_context_data['total']
            
            return JsonResponse({
                'success': True,
                'cart_total': cart_total,
                'cart_price': float(cart_price)
            })
        
        return JsonResponse({
            'success': False,
            'message': 'Item not found in cart'
        })

@require_POST
def remove_from_cart(request, item_id):
    """
    Remove an item from the cart via AJAX.
    
    Supports both authenticated users (database cart) and anonymous users (session cart).
    
    Args:
        item_id (str): For authenticated users: database CartItem ID
                      For anonymous users: session cart key (e.g., "22" or "22_15")
                      
    Returns:
        JsonResponse: Success status with updated cart totals
    """
    if request.user.is_authenticated:
        # Handle database cart
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart = cart_item.cart
        cart_item.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Item removed from cart',
            'cart_total': cart.total_items,
            'cart_price': float(cart.total_price)
        })
    else:
        # Handle session cart
        session_cart = request.session.get('cart', {})
        
        # Convert item_id to string to ensure consistent key comparison
        item_key = str(item_id)
        
        if item_key in session_cart:
            del session_cart[item_key]
            request.session['cart'] = session_cart
            request.session.modified = True
            
            # Recalculate totals using context processor
            cart_total = sum(item_data.get('quantity', 1) for item_data in session_cart.values())
            cart_context_data = cart_contents(request)
            cart_price = cart_context_data['total']
            
            return JsonResponse({
                'success': True,
                'message': 'Item removed from cart',
                'cart_total': cart_total,
                'cart_price': float(cart_price)
            })
        
        return JsonResponse({
            'success': False,
            'message': 'Item not found in cart'
        })