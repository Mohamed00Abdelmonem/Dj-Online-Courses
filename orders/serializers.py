from rest_framework import serializers
from .models import Cart, CartDetial



class CartDetailSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = CartDetial
        fields = '__all__'




class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSeriaizer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'

