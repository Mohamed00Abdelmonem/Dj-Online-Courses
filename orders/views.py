from django.shortcuts import render, redirect
from .models import Cart, CartDetial
from courses.models import Course

def add_to_cart(request):
    course = Course.objects.get(id=request.POST['course_id'])
    cart = Cart.objects.get(user= request.user, status= 'InProgress')
    cart_detail, created = CartDetial.objects.get_or_create(cart=cart, course=course)

    cart_detail.total = round(int(1)* course.price,2)
    cart_detail.save()
    return redirect(f'/courses/{course.slug}')


def cart(request):
    return render(request, 'cart.html')




def checkout(request):
    return render (request, 'checkout.html')


