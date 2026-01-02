from django.urls import path

from . import views, webhooks

app_name = "checkout"

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("review/", views.review_order, name="review"),
    path("payment/", views.payment, name="payment"),
    path("process-payment/", views.process_payment, name="process_payment"),
    path(
        "success/<str:order_number>/",
        views.checkout_success,
        name="checkout_success",
    ),
    path("webhook/", webhooks.webhook, name="webhook"),
]
