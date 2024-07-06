from rest_framework import serializers
from .models import Cart, CartDetial
from courses.models import Course

class CourseCartSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title','image', 'price']

class CartDetailSeriaizer(serializers.ModelSerializer):
    course = CourseCartSeriaizer()
    class Meta:
        model = CartDetial
        fields = '__all__'




class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSeriaizer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'

