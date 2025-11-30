import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from cart.context_processors import cart_contents
from .forms import OrderForm
from .models import Order, OrderItem

# Configure Stripe API key from Django settings
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """
    Handle checkout process with Stripe payment integration.
    
    Requires user authentication for license key delivery and game account linking.
    Creates Stripe PaymentIntent and processes order after successful payment.
    
    Flow:
    1. Create/validate cart contents
    2. Generate Stripe PaymentIntent with order total
    3. Display checkout form with payment elements
    4. Process successful payment and create order
    5. Redirect to confirmation page
    """
    
    # DEVELOPMENT ONLY: Auto-populate cart with base game for testing
    # TODO: Remove when implementing proper cart/product browsing
    # In checkout view, for testing different platforms:
    if not request.session.get('cart'):
        from catalog.models import Product
        base_game = Product.objects.filter(product_type=Product.BASE_GAME).first()
        if base_game:
            request.session['cart'] = {
                'item_1': {'product_id': base_game.id, 'quantity': 1, 'platform': 'NINTENDO'},  # Test different platforms
            }

    # Get cart contents via context processor
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
            
            # Set calculated totals and user association
            order.total_amount = cart['grand_total']
            order.user = request.user
                
            # Store Stripe PaymentIntent ID for tracking and webhooks
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            
            # Create order items with snapshotted product data
            _create_order_items(order, cart['cart_items'])
            
            # Clear cart after successful order creation
            request.session['cart'] = {}
            
            return redirect('checkout:checkout_success', order_number=order.order_number)
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # GET request: Create PaymentIntent and show form
        total = cart['grand_total']
        stripe_total = round(total * 100)  # Convert pounds to pence for Stripe
        
        try:
            # Create PaymentIntent with metadata for webhook processing
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                metadata={
                    'cart': str(request.session.get('cart', {})),
                    'username': request.user.username,
                },
            )
        except stripe.error.StripeError as e:
            messages.error(request, f'Stripe error: {e}')
            return redirect('catalog:product_list')
        
        # Pre-fill form with authenticated user data
        initial_data = {
            'full_name': request.user.get_full_name() or f"{request.user.first_name} {request.user.last_name}".strip(),
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


@login_required
def checkout_success(request, order_number):
    """
    Display order confirmation and process digital fulfillment.
    
    For portfolio demonstration, processes fulfillment immediately.
    In production, this would be handled by Stripe webhooks for reliability.
    """
    order = get_object_or_404(Order, order_number=order_number)
    
    # Security: Ensure user can only view their own orders
    if order.user != request.user:
        messages.error(request, "You don't have permission to view this order.")
        return redirect('catalog:product_list')
    
    # Process digital fulfillment (license keys, credits, email confirmation)
    # NOTE: In production, this would be triggered by Stripe webhooks
    from checkout.webhook_handler import StripeWH_Handler
    handler = StripeWH_Handler(request)
    handler._process_digital_fulfillment(order)
    handler._send_confirmation_email(order)
    
    messages.success(request, f'Order processed successfully! Order number: {order.order_number}. '
                             f'A confirmation email will be sent to {order.email}.')
    
    context = {'order': order}
    return render(request, 'checkout/checkout_success.html', context)


def _create_order_items(order, cart_items):
    """
    Create OrderItem records from cart data with product snapshots.
    
    Preserves product information at time of purchase for order history integrity.
    This ensures order data remains intact even if products are modified later.
    """
    for cart_item in cart_items:
        product = cart_item['product']
        variant = cart_item.get('variant')
        
        # Build variant description for order records
        variant_details = ""
        if variant:
            variant_details = f"{variant.get_platform_display()} {variant.get_edition_display()}"
        
        # Capture platform from cart for license key generation
        platform = cart_item.get('platform', 'PC')  # Get platform from cart or default to PC
        
        # Modify product name to include platform for license key generation
        product_name = product.name
        if platform and platform != 'PC':
            product_name = f"{product.name} ({platform})"
        
        # Create order item with snapshotted data
        OrderItem.objects.create(
            order=order,
            product=product,                    # FK reference
            variant=variant,                    # FK reference  
            product_name=product_name,          # Snapshotted data
            product_sku=product.sku,            # Snapshotted data
            variant_details=variant_details,    # Snapshotted data
            quantity=cart_item['quantity'],
            unit_price=cart_item['price'],      # Snapshotted price
        )