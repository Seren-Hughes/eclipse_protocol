import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from cart.context_processors import cart_contents
from .forms import OrderForm
from .models import Order, OrderItem

# Configure Stripe API key from Django settings
stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """
    Display checkout form and create Stripe PaymentIntent.
    
    Creates a Stripe PaymentIntent before showing the form,
    allowing secure client-side payment processing.
    """
    
    # TEMPORARY: Create test cart if empty (for development testing)
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

    # Get cart contents using context processor
    cart = cart_contents(request)
    
    # Redirect if cart is empty
    if not cart['cart_items']:
        messages.error(request, "Your cart is empty.")
        return redirect('catalog:product_list')

    if request.method == 'POST':
        # Process completed payment and create order
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            
            # Set order totals from cart
            order.total_amount = cart['grand_total']
            
            # Link to user if authenticated
            if request.user.is_authenticated:
                order.user = request.user
                
            # Store Stripe PaymentIntent ID for tracking
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            
            # Create order items with snapshoted product data
            _create_order_items(order, cart['cart_items'])
            
            # Clear cart after successful order processing
            request.session['cart'] = {}
            
            return redirect('checkout:checkout_success', order_number=order.order_number)
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # GET request: create Stripe PaymentIntent and show form
        total = cart['grand_total']
        stripe_total = round(total * 100)  # Convert pounds to pence for Stripe
        
        try:
            # Create Stripe PaymentIntent with cart metadata
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                metadata={
                    'cart': str(request.session.get('cart', {})),
                    'username': request.user.username if request.user.is_authenticated else 'guest',
                },
            )
        except stripe.error.StripeError as e:
            messages.error(request, f'Stripe error: {e}')
            return redirect('catalog:product_list')
        
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
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Display order confirmation page after successful payment.
    """
    order = get_object_or_404(Order, order_number=order_number)
    
    # Security: Only allow order owner or anonymous users to view their recent order
    if order.user and order.user != request.user:
        messages.error(request, "You don't have permission to view this order.")
        return redirect('catalog:product_list')
    
    # display success confirmation message
    messages.success(request, f'Order processed successfully! Order number: {order.order_number}. '
                             f'A confirmation email will be sent to {order.email}.')
    
    context = {
        'order': order,
    }
    
    return render(request, 'checkout/checkout_success.html', context)


def _create_order_items(order, cart_items):
    """
    Helper function to create OrderItem objects from cart data.
    
    Snapshots current product/variant information to preserve
    order history even if products change later.

    Args:
        order: Order instance to associate items with
        cart_items: List of cart item dictionaries from cart context processor
    """
    for cart_item in cart_items:
        product = cart_item['product']
        variant = cart_item.get('variant')
        
        # Build variant description for order history
        variant_details = ""
        if variant:
            variant_details = f"{variant.get_platform_display()} {variant.get_edition_display()}"
        
        # Create order item with snapshotted data
        OrderItem.objects.create(
            order=order,
            product=product,
            variant=variant,
            product_name=product.name,          # Snapshot current name
            product_sku=product.sku,            # Snapshot current SKU
            variant_details=variant_details,    # Snapshot variant info
            quantity=cart_item['quantity'],
            unit_price=cart_item['price'],      # Snapshot current price
            # total_price calculated automatically in model save() method
        )