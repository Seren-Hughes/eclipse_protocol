from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact-confirmation/', views.contact_confirmation, name='contact_confirmation'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('faqs/', views.faqs, name='faqs'),
]