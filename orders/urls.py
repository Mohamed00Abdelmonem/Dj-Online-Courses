from django.urls import path
from . import views


app_name = 'orders'


urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout')
]