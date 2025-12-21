import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import now
import json
from cart.context_processors import cart_contents
from cart.models import Cart
from accounts.models import Address
from .forms import OrderForm
from .models import Order, OrderItem

# Configure Stripe API key from Django settings
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """
    Handle checkout billing address step.
    
    Collects billing address information and saves it for the next step.
    Payment processing moved to separate step.
    """
    
    # Get cart contents - handle both authenticated (database) and session carts
    if request.user.is_authenticated:
        try:
            db_cart = Cart.objects.get(user=request.user)
            cart_items = list(db_cart.items.select_related('product', 'variant', 'product__currency').all())
            
            # Convert database cart items to the format expected by templates
            formatted_cart_items = []
            total = 0
            product_count = 0
            
            for db_item in cart_items:
                item_data = {
                    'item_id': str(db_item.id),
                    'product': db_item.product,
                    'variant': db_item.variant,
                    'quantity': db_item.quantity,
                    'price': db_item.effective_price,
                    'line_total': db_item.line_total,
                    'display_name': db_item.product.name,
                }
                
                # Add variant info to display name if present
                if db_item.variant:
                    item_data['display_name'] += f" - {db_item.variant.get_platform_display()} {db_item.variant.get_edition_display()}"
                
                formatted_cart_items.append(item_data)
                total += db_item.line_total
                product_count += db_item.quantity
            
            # Create cart context similar to session cart
            cart = {
                'cart_items': formatted_cart_items,
                'total': total,
                'product_count': product_count,
                'delivery': 0,
                'grand_total': total,
                'shipping_required': False,
            }
            
        except Cart.DoesNotExist:
            # No database cart exists, fall back to session cart
            cart = cart_contents(request)
    else:
        # For anonymous users, use session cart
        cart = cart_contents(request)
    
    # Redirect if cart is empty
    if not cart['cart_items']:
        messages.error(request, "Your cart is empty.")
        return redirect('home')

    # Get user's saved billing addresses
    saved_addresses = Address.objects.filter(user=request.user, address_type=Address.BILLING)
    default_address = saved_addresses.first()  # Use most recent as default
    
    if request.method == 'POST':
        # Process billing address form
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save address if user requested it
            save_address = request.POST.get('save_address')
            if save_address and not saved_addresses.exists():
                Address.objects.create(
                    user=request.user,
                    address_type=Address.BILLING,
                    full_name=form.cleaned_data['full_name'],
                    address_line_1=form.cleaned_data['street_address_1'],
                    address_line_2=form.cleaned_data['street_address_2'] or '',
                    city=form.cleaned_data['city'],
                    postcode=form.cleaned_data['postcode'],
                    country=form.cleaned_data['country'],
                )
            
            # Store billing address in session for next step
            request.session['billing_address'] = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'street_address_1': form.cleaned_data['street_address_1'],
                'street_address_2': form.cleaned_data['street_address_2'],
                'city': form.cleaned_data['city'],
                'postcode': form.cleaned_data['postcode'],
                'country': form.cleaned_data['country'],
                'phone_number': form.cleaned_data.get('phone_number', ''),
            }
            
            # Redirect to review step
            return redirect('checkout:review')
            
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # GET request: Show form
        # Pre-fill form with user data - use saved address if available
        if default_address:
            initial_data = {
                'full_name': default_address.full_name,
                'email': request.user.email,
                'street_address_1': default_address.address_line_1,
                'street_address_2': default_address.address_line_2,
                'city': default_address.city,
                'postcode': default_address.postcode,
                'country': default_address.country,
            }
        else:
            initial_data = {
                'full_name': request.user.get_full_name() or f"{request.user.first_name} {request.user.last_name}".strip(),
                'email': request.user.email,
            }
        form = OrderForm(initial=initial_data)

    context = {
        'form': form,
        'cart': cart,
        'has_saved_address': saved_addresses.exists(),
        'saved_addresses': saved_addresses,
        'using_saved_address': bool(default_address),
    }
    
    return render(request, 'checkout/checkout.html', context)


@login_required
def review_order(request):
    """
    Review order before payment.
    
    Shows billing address and order summary for final confirmation.
    """
    
    # Check if billing address is in session
    billing_address_data = request.session.get('billing_address')
    if not billing_address_data:
        messages.error(request, "Please complete the billing address first.")
        return redirect('checkout:checkout')
    
    # Convert dictionary to object-like structure for template access
    from types import SimpleNamespace
    billing_address = SimpleNamespace(**billing_address_data)
    
    # Get cart contents
    if request.user.is_authenticated:
        try:
            db_cart = Cart.objects.get(user=request.user)
            cart_items = list(db_cart.items.select_related('product', 'variant', 'product__currency').all())
            
            formatted_cart_items = []
            total = 0
            product_count = 0
            
            for db_item in cart_items:
                item_data = {
                    'item_id': str(db_item.id),
                    'product': db_item.product,
                    'variant': db_item.variant,
                    'quantity': db_item.quantity,
                    'price': db_item.effective_price,
                    'line_total': db_item.line_total,
                    'display_name': db_item.product.name,
                }
                
                if db_item.variant:
                    item_data['display_name'] += f" - {db_item.variant.get_platform_display()} {db_item.variant.get_edition_display()}"
                
                formatted_cart_items.append(item_data)
                total += db_item.line_total
                product_count += db_item.quantity
            
            cart = {
                'cart_items': formatted_cart_items,
                'total': total,
                'product_count': product_count,
                'delivery': 0,
                'grand_total': total,
                'shipping_required': False,
            }
            
        except Cart.DoesNotExist:
            cart = cart_contents(request)
    else:
        cart = cart_contents(request)
    
    # Redirect if cart is empty
    if not cart['cart_items']:
        messages.error(request, "Your cart is empty.")
        return redirect('home')
    
    context = {
        'billing_address': billing_address,
        'cart': cart,
    }
    
    return render(request, 'checkout/review_order.html', context)


@login_required  
def payment(request):
    """
    Handle payment processing with Stripe.
    
    Creates PaymentIntent and shows payment form.
    """
    
    # Check if billing address is in session
    billing_address_data = request.session.get('billing_address')
    if not billing_address_data:
        messages.error(request, "Please complete the billing address first.")
        return redirect('checkout:checkout')
    
    # Convert dictionary to object-like structure for template access
    from types import SimpleNamespace
    billing_address = SimpleNamespace(**billing_address_data)
    
    # Get cart contents
    if request.user.is_authenticated:
        try:
            db_cart = Cart.objects.get(user=request.user)
            cart_items = list(db_cart.items.select_related('product', 'variant', 'product__currency').all())
            
            formatted_cart_items = []
            total = 0
            product_count = 0
            
            for db_item in cart_items:
                item_data = {
                    'item_id': str(db_item.id),
                    'product': db_item.product,
                    'variant': db_item.variant,
                    'quantity': db_item.quantity,
                    'price': db_item.effective_price,
                    'line_total': db_item.line_total,
                    'display_name': db_item.product.name,
                }
                
                if db_item.variant:
                    item_data['display_name'] += f" - {db_item.variant.get_platform_display()} {db_item.variant.get_edition_display()}"
                
                formatted_cart_items.append(item_data)
                total += db_item.line_total
                product_count += db_item.quantity
            
            cart = {
                'cart_items': formatted_cart_items,
                'total': total,
                'product_count': product_count,
                'delivery': 0,
                'grand_total': total,
                'shipping_required': False,
            }
            
        except Cart.DoesNotExist:
            cart = cart_contents(request)
    else:
        cart = cart_contents(request)
    
    # Redirect if cart is empty
    if not cart['cart_items']:
        messages.error(request, "Your cart is empty.")
        return redirect('home')
    
    # Create Stripe PaymentIntent
    stripe_total = round(cart['grand_total'] * 100)  # convert to cents
    
    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'user_id': request.user.id,
                'billing_address': str(billing_address_data),  # Store as string for reference
            },
        )
    except stripe.error.StripeError as e:
        messages.error(request, f'Stripe error: {e}')
        return redirect('checkout:review')
    
    context = {
        'cart': cart,
        'billing_address': billing_address,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    
    return render(request, 'checkout/payment.html', context)


@login_required
def process_payment(request):
    """
    Process the completed payment and create order.
    """
    
    if request.method != 'POST':
        return redirect('checkout:payment')
    
    # Get billing address and cart data
    billing_address_data = request.session.get('billing_address')
    if not billing_address_data:
        messages.error(request, "Session expired. Please start checkout again.")
        return redirect('checkout:checkout')
    
    # Convert dictionary to object-like structure for template access
    from types import SimpleNamespace
    billing_address = SimpleNamespace(**billing_address_data)
    
    # Get cart contents
    if request.user.is_authenticated:
        try:
            db_cart = Cart.objects.get(user=request.user)
            cart_items = list(db_cart.items.select_related('product', 'variant', 'product__currency').all())
            
            formatted_cart_items = []
            total = 0
            
            for db_item in cart_items:
                item_data = {
                    'item_id': str(db_item.id),
                    'product': db_item.product,
                    'variant': db_item.variant,
                    'quantity': db_item.quantity,
                    'price': db_item.effective_price,
                    'line_total': db_item.line_total,
                }
                
                formatted_cart_items.append(item_data)
                total += db_item.line_total
            
            cart = {
                'cart_items': formatted_cart_items,
                'grand_total': total,
            }
            
        except Cart.DoesNotExist:
            cart = cart_contents(request)
    else:
        cart = cart_contents(request)
    
    try:
        # Create cart snapshot for order history
        cart_snapshot = {
            'items': [
                {
                    'product_id': str(item['product'].id),
                    'product_name': item['product'].name,
                    'product_sku': item['product'].sku,
                    'variant_id': str(item['variant'].id) if item['variant'] else None,
                    'variant_details': {
                        'platform': item['variant'].get_platform_display() if item['variant'] else None,
                        'edition': item['variant'].get_edition_display() if item['variant'] else None,
                    } if item['variant'] else None,
                    'quantity': item['quantity'],
                    'unit_price': str(item['price']),
                    'line_total': str(item['line_total']),
                }
                for item in cart['cart_items']
            ],
            'cart_total': str(cart['grand_total']),
            'purchase_date': now().isoformat(),
        }
        
        # Create order with PAID status if payment was successful
        order = Order.objects.create(
            user=request.user,
            full_name=billing_address.full_name,
            email=billing_address.email,
            street_address_1=billing_address.street_address_1,
            street_address_2=getattr(billing_address, 'street_address_2', ''),
            city=billing_address.city,
            postcode=billing_address.postcode,
            country=billing_address.country,
            phone_number=getattr(billing_address, 'phone_number', ''),
            total_amount=cart['grand_total'],
            stripe_pid=request.POST.get('client_secret', '').split('_secret')[0],
            original_cart=json.dumps(cart_snapshot),
            payment_status=Order.PAYMENT_PAID,  # Set as paid Stripe confirmed payment
            delivery_status=Order.DELIVERY_SENT,  # digital products instantly delivered
        )
        
        # Create order items
        _create_order_items(order, cart['cart_items'])
        
        # Clear cart and session
        if request.user.is_authenticated:
            try:
                db_cart = Cart.objects.get(user=request.user)
                db_cart.items.all().delete()
            except Cart.DoesNotExist:
                pass
        else:
            request.session['cart'] = {}
        
        # Clear billing address from session
        if 'billing_address' in request.session:
            del request.session['billing_address']
        
        return redirect('checkout:checkout_success', order_number=order.order_number)
        
    except Exception as e:
        print(f"ERROR in process_payment: {e}")
        import traceback
        traceback.print_exc()
        messages.error(request, "There was an error processing your order. Please contact support.")
        return redirect('checkout:payment')


@login_required
def checkout_success(request, order_number):
    """
    Display order confirmation and process digital fulfillment.
    """
    try:
        order = get_object_or_404(Order, order_number=order_number)
        
        # Ensure the order belongs to the logged-in user
        if order.user != request.user:
            messages.error(request, "You don't have permission to view this order.")
            return redirect('home')
        
        # Process digital fulfillment (license keys, credits, email confirmation)
        try:
            from checkout.webhook_handler import StripeWH_Handler
            handler = StripeWH_Handler(request)
            handler._process_digital_fulfillment(order)
            handler._send_confirmation_email(order)
        except Exception as e:
            print(f"ERROR in digital fulfillment: {e}")
            # Don't fail the whole page if fulfillment has issues
        
        messages.success(request, f'Order processed successfully! Order number: {order.order_number}. '
                                 f'A confirmation email will be sent to {order.email}.')
        
        context = {'order': order}
        return render(request, 'checkout/checkout_success.html', context)
        
    except Exception as e:
        print(f"ERROR in checkout_success: {e}")
        import traceback
        traceback.print_exc()
        messages.error(request, "There was an error loading your order confirmation.")
        return redirect('home')


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
        platform = cart_item.get('platform', 'PC')
        
        # Modify product name to include platform for license key generation
        product_name = product.name
        if platform and platform != 'PC':
            product_name = f"{product.name} ({platform})"
        
        # Create order item with snapshotted data
        OrderItem.objects.create(
            order=order,
            product=product,
            variant=variant,
            product_name=product_name,
            product_sku=product.sku,
            variant_details=variant_details,
            quantity=cart_item['quantity'],
            unit_price=cart_item['price'],
        )