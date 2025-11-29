from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from cart.context_processors import cart_contents
from .forms import OrderForm
from .models import Order, OrderItem

# Create your views here.

def checkout(request):
    """
    Display checkout form and handle order creation.
    
    Temporary basic form without Stripe integration for development testing.
    
    Includes temporary test cart creation for development testing.
    """

    # TEMPORARY: Create test cart if empty (for development testing)
    # This will be removed once proper "Add to Cart" functionality is implemented
    if not request.session.get('cart'):
        from catalog.models import Product
        product = Product.objects.first()
        if product:
            request.session['cart'] = {
                'item_1': {
                    'product_id': product.id,
                    'quantity': 1
                }
            }

    # Get cart contents
    cart = cart_contents(request)
    
    # Redirect if cart is empty
    if not cart['cart_items']:
        messages.error(request, "Your cart is empty.")
        return redirect('catalog:product_list') 
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            
            # Set order totals from cart
            order.total_amount = cart['grand_total']
            
            # Link to user if authenticated
            if request.user.is_authenticated:
                order.user = request.user
            
            order.save()
            
            # Create order items from cart
            _create_order_items(order, cart['cart_items'])
            
            # Clear cart after successful order creation
            request.session['cart'] = {}
            
            messages.success(request, f'Order {order.order_number} created successfully!')
            return redirect('checkout:checkout_success', order_number=order.order_number)
    else:
        # Pre-fill form with user data if authenticated
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'full_name': request.user.get_full_name(),
                'email': request.user.email,
            }
        form = OrderForm(initial=initial_data)
    
    context = {
        'form': form,
        'cart': cart,
    }
    
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Display order confirmation page.
    """
    order = get_object_or_404(Order, order_number=order_number)
    
    # Security: Only allow order owner or anonymous users to view their recent order
    if order.user and order.user != request.user:
        messages.error(request, "You don't have permission to view this order.")
        return redirect('catalog:product_list')
    
    context = {
        'order': order,
    }
    
    return render(request, 'checkout/checkout_success.html', context)


def _create_order_items(order, cart_items):
    """
    Helper function to create OrderItem objects from cart data.
    
    Snapshots current product/variant information to preserve
    order history even if products change later.
    """
    for cart_item in cart_items:
        product = cart_item['product']
        variant = cart_item.get('variant')
        
        # Determine variant details for display
        variant_details = ""
        if variant:
            variant_details = f"{variant.get_platform_display()} {variant.get_edition_display()}"
        
        OrderItem.objects.create(
            order=order,
            product=product,
            variant=variant,
            product_name=product.name,
            product_sku=product.sku,
            variant_details=variant_details,
            quantity=cart_item['quantity'],
            unit_price=cart_item['price'],
            # total_price calculated automatically in model save()
        )