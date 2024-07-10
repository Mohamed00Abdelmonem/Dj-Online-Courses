from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer, CouponSerializer
from .models import Cart, CartDetial, Coupon
from courses.models import Course
import datetime





# ____________________________________________________________________________________________-

class CartDetailCreateAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status='InProgress')
        data = CartSerializer(cart).data  # convert form list to json
        return Response({'cart': data})
    

    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        course = Course.objects.get(id=request.data['course_id'])
        cart = Cart.objects.get(user=user, status='InProgress') 
        cart_detail, created = CartDetial.objects.get_or_create(cart=cart, course=course)
        cart_detail.course = course
        cart_detail.save() 
        cart = Cart.objects.get(user=user, status='InProgress')
        data = CartSerializer(cart).data 
        return Response({'message':'Course added successfully', 'cart':data})


    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user, status='InProgress') 
        course = Course.objects.get(id=request.data['course_id'])
        cart_detail = CartDetial.objects.get(cart=cart, course=course)
        cart_detail.delete()
        cart = Cart.objects.get(user=user, status='InProgress')
        data = CartSerializer(cart).data 
        return Response({'message':'Course {course_id} Delete successfully', 'cart':data})


# ____________________________________________________________________________________________-



class ApplayCouponAPI(generics.GenericAPIView):
    def post(self,request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user, status='InProgress')

        coupon = get_object_or_404(Coupon, code=request.data['coupon_code']) #   404
        # coupon = Coupon.objects.get(code=request.data['coupon_code']) # Error

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()

            if today_date >= coupon.start_date.date() and today_date <= coupon.end_date.date():
            # if today_date >= coupon_start_date and today_date <= coupon_end_date:
                coupon_value  = cart.cart_total() * coupon.discount/100
                cart_total = cart.cart_total() - coupon_value

                coupon.quantity -= 1
                coupon.save()

                cart.coupon = coupon
                cart.total_after_coupon = cart_total
                cart.save()
                cart = Cart.objects.get(user=user, status='InProgress')
                data = CartSerializer(cart).data

                return Response({'message':'Coupon Applied Successfully', 'cart':data})
            
            else:
                return Response({'message':'Coupon date are not valid'})
            
        else:
             return Response({'message':'No Coupon Found'})
        


# ____________________________________________________________________________________________-
