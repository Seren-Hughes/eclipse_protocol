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
            from django.core.mail import EmailMultiAlternatives
            from django.utils.html import strip_tags
            
            # Build email context with product type flags
            context = {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'has_base_games': order.items.filter(product__product_type='base_game').exists(),
                'has_currency': order.items.filter(product__product_type='currency').exists(),
            }
            
            # Plain text subject
            subject = render_to_string(
                'checkout/confirmation_emails/confirmation_email_subject.txt',
                context
            ).strip()
            
            # HTML body
            html_body = render_to_string(
                'checkout/confirmation_emails/confirmation_email_body.html',
                context
            )
            
            # Plain text fallback
            plain_body = render_to_string(
                'checkout/confirmation_emails/confirmation_email_body.txt',
                context
            )

            # Send multipart email
            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[order.email]
            )
            email.attach_alternative(html_body, "text/html")
            email.send(fail_silently=False)
        
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
        """Generate platform-specific license key for base game products."""
        try:
            # Use the platform from the variant if available, otherwise default to PC
            platform = 'PC'  # Default fallback
            
            if item.variant:
                # Use the actual platform from the variant
                platform = item.variant.platform.upper()
            else:
                # Fallback: Check if product name contains platform hints
                product_name = item.product_name.upper()
                if 'NINTENDO' in product_name or 'SWITCH' in product_name:
                    platform = 'NINTENDO'
                elif 'XBOX' in product_name:
                    platform = 'XBOX'
                elif 'STEAM' in product_name or 'PC' in product_name:
                    platform = 'PC'
            
            # Generate platform-specific key
            key_code = self._generate_key_code(item.product, platform)
            
            # Create license key record
            license_key = LicenseKey.objects.create(
                user=order.user,
                order_item=item,
                product=item.product,
                variant=item.variant,
                key_code=key_code,
                platform=platform,
                status='active'
            )
        
            return license_key
        
        except Exception as e:
            return None

    def _generate_key_code(self, product, platform):
        """
        Generate platform-specific license keys
        
        PC (Steam-style): XXXXX-XXXXX-XXXXX-XXXXX (20 chars, 4 blocks of 5)
        Xbox: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX (25 chars, 5 blocks of 5) 
        Nintendo Switch: AAAA-BBBB-CCCC-DDDD (16 chars, 4 blocks of 4)
        """
        import random
        import string
        
        def generate_pc_key():
            """Generate Steam-style key: XXXXX-XXXXX-XXXXX-XXXXX"""
            groups = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(4)]
            return '-'.join(groups)
        
        def generate_xbox_key():
            """Generate Xbox-style key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX"""
            groups = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5)]
            return '-'.join(groups)
        
        def generate_switch_key():
            """Generate Nintendo Switch-style key: AAAA-BBBB-CCCC-DDDD"""
            groups = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4)]
            return '-'.join(groups)
        
        
        # Platform-specific key generation
        key_generators = {
            'PC': generate_pc_key,
            'STEAM': generate_pc_key,
            'XBOX': generate_xbox_key,
            'NSW': generate_switch_key,
            'NINTENDO': generate_switch_key,
            'SWITCH': generate_switch_key,
        }
        
        # Generate key with collision checking
        generator = key_generators.get(platform.upper(), generate_pc_key)
        
        while True:
            key_code = generator()

            # Ensure uniqueness across all platforms
            if not LicenseKey.objects.filter(key_code=key_code).exists():
                return key_code

