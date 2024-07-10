from django.urls import path
from . import views
from .api import CartDetailCreateAPI, ApplayCouponAPI

app_name = 'orders'


urlpatterns = [
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('<int:id>/remove-form-cart', views.remove_from_cart),
    path('checkout', views.checkout, name='checkout'),


    # api
    path('api/<str:username>/cart', CartDetailCreateAPI.as_view()),
    path('api/cart/<str:username>/apply-coupon', ApplayCouponAPI.as_view()),
]