from django.urls import path
from . import views, webhooks

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<str:order_number>/', views.checkout_success, name='checkout_success'),
    path('webhook/', webhooks.webhook, name='webhook'),
]