from django.urls import path
from . import views

app_name = 'webshop'

urlpatterns = [
    path('', views.shop_home, name="shop-home"),
    path('box/<slug>/', views.BoxDetailView.as_view(), name="shop-box"),
    path('cart/', views.shop_cart, name="shop-cart"),
    path('add-to-cart/<slug>/', views.add_to_cart, name="shop-add-cart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name="shop-remove-cart"),
    path('checkout/', views.shop_checkout, name="shop-checkout"),
    path('about/', views.shop_about, name="shop-about"),
    path('boxes/', views.BoxShopView.as_view(), name="shop-boxes"),
]
