from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.search_results, name='search_results'),
    path('currency/', views.currency_detail, name='currency_detail'),
    path('currency/<slug:product_slug>/', views.currency_detail, name='currency_detail_with_selection'),
    path('base-game/<slug:product_slug>/', views.edition_detail, name='edition_detail'),
    path('base-game/<slug:product_slug>/<slug:platform>/<slug:edition>/', views.edition_detail, name='edition_detail_variant'),
]