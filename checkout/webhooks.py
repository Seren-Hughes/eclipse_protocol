from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import stripe

from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe.

    Verifies webhook signature for security and routes events to appropriate handlers.
    Handles payment confirmations and failures for reliable order processing.
    """
    # Setup Stripe configuration
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify signature
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except (ValueError, stripe.error.SignatureVerificationError) as e:
        return HttpResponse(content=str(e), status=400)
    except Exception as e:
        return HttpResponse(content=str(e), status=400)

    # Route webhook events to handler methods
    handler = StripeWH_Handler(request)
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_payment_failed,
    }

    # Execute appropriate handler or use generic fallback
    event_handler = event_map.get(event["type"], handler.handle_event)
    response = event_handler(event)

    return response
