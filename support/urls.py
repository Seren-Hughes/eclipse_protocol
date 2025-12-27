from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]