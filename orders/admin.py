from django.contrib import admin
from .models import Cart, CartDetial, Order, OrderDetail, Coupon
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartDetial)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Coupon)