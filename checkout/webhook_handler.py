from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderItem, LicenseKey
from catalog.models import Product
import time
import json


class StripeWH_Handler:
    """
    Handle Stripe webhooks for payment processing and digital fulfillment.
    
    Provides reliable order processing even if user closes browser during checkout.
    Handles license key generation and email confirmations automatically.
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send order confirmation email with product-specific messaging."""
        try:
            # Build email context with product type flags
            context = {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'has_base_games': order.items.filter(product__product_type='base_game').exists(),
                'has_currency': order.items.filter(product__product_type='currency').exists(),
            }
            
            subject = render_to_string(
                'checkout/confirmation_emails/confirmation_email_subject.txt',
                context).strip()
            body = render_to_string(
                'checkout/confirmation_emails/confirmation_email_body.txt',
                context)

            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [order.email], fail_silently=False)
            
        except Exception as e:
            print(f"ERROR: Failed to send confirmation email: {e}")

    def handle_event(self, event):
        """Handle generic/unknown webhook events."""
        return HttpResponse(content=f'Unhandled webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle successful payment webhook from Stripe.
        
        Locates the order by PaymentIntent ID and processes digital fulfillment.
        Includes retry logic for cases where order creation is delayed.
        """
        intent = event.data.object
        pid = intent.id

        # Locate order with retry logic (handles race conditions)
        order = None
        for attempt in range(1, 6):
            try:
                order = Order.objects.get(stripe_pid=pid)
                break
            except Order.DoesNotExist:
                if attempt == 5:
                    return HttpResponse(content=f'Order not found for payment {pid}', status=400)
                time.sleep(1)
        
        # Process digital fulfillment and send confirmation
        self._process_digital_fulfillment(order)
        self._send_confirmation_email(order)
        
        return HttpResponse(content=f'Webhook processed successfully for order {order.order_number}', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle failed payment webhook from Stripe."""
        return HttpResponse(content=f'Payment failed webhook received: {event["type"]}', status=200)

    def _process_digital_fulfillment(self, order):
        """
        Process digital product fulfillment based on product types.
        
        - Base games: Generate license keys for platform redemption
        - Currency: Log credit application (would integrate with game API in production)
        """
        for item in order.items.all():
            if item.product.product_type == 'currency':
                self._process_currency_purchase(order, item)
            elif item.product.product_type == 'base_game':
                self._generate_license_key(order, item)

    def _process_currency_purchase(self, order, item):
        """
        Process in-game currency purchase.
        
        Portfolio note: In production, this would call the game API to credit
        the user's account. For demonstration, the transaction is logged.
        """
        try:
            currency_product = item.product.currency_details
            credit_amount = currency_product.credit_amount
            print(f"CURRENCY: {credit_amount} credits applied to {order.user.username}'s account")
            
            # Production implementation would be:
            # game_api.add_credits(user_id=order.user.id, amount=credit_amount)
            
        except Exception as e:
            print(f"ERROR: Currency processing failed: {e}")

    def _generate_license_key(self, order, item):
        """Generate unique license key for base game products."""
        try:
            platform = 'PC'  # Default platform (could be determined from variant)
            key_code = self._generate_key_code(item.product, platform)
            
            # Create license key record
            LicenseKey.objects.create(
                user=order.user,
                order_item=item,
                product=item.product,
                variant=item.variant,
                key_code=key_code,
                platform=platform,
                status='active'
            )
            
        except Exception as e:
            print(f"ERROR: License key generation failed: {e}")

    def _generate_key_code(self, product, platform):
        """
        Generate unique license key in format: PREFIX-XXXX-XXXX-XXXX-XXXX
        
        Prefix varies by platform (EP=PC, EPX=Xbox, EPS=PlayStation, EPN=Nintendo)
        Ensures uniqueness across all existing license keys.
        """
        import random
        import string
        
        # Platform-specific prefixes
        prefixes = {
            'PC': 'EP', 'XBOX': 'EPX', 'PS5': 'EPS', 'NSW': 'EPN'
        }
        prefix = prefixes.get(platform, 'EP')
        
        # Generate unique key with collision checking
        while True:
            groups = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4)]
            key_code = f"{prefix}-{'-'.join(groups)}"
            
            if not LicenseKey.objects.filter(key_code=key_code).exists():
                return key_code