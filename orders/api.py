from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer
from .models import Cart, CartDetial
from courses.models import Course


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




    