from rest_framework import serializers
from .models import Cart, CartDetial, Coupon
from courses.models import Course







# ____________________________________________________________________________________________-

class CourseCartSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title','image', 'price']
# ____________________________________________________________________________________________-

class CartDetailSeriaizer(serializers.ModelSerializer):
    course = CourseCartSeriaizer()
    class Meta:
        model = CartDetial
        fields = '__all__'


# ____________________________________________________________________________________________-


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSeriaizer(many=True)
    coupon_code = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'status', 'coupon_code', 'total_after_coupon', 'cart_detail']

    def get_coupon_code(self, obj):
        return obj.coupon.code if obj.coupon else None

    def get_user(self, obj):
        return obj.user.username if obj.user else None

# ____________________________________________________________________________________________-

    
    
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

    

# ____________________________________________________________________________________________-
