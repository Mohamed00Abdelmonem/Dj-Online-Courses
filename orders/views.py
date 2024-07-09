from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Cart, CartDetial, Coupon
from courses.models import Course
import datetime




def add_to_cart(request):
    course = Course.objects.get(id=request.POST['course_id'])
    cart = Cart.objects.get(user= request.user, status= 'InProgress')
    cart_detail, created = CartDetial.objects.get_or_create(cart=cart, course=course)

    cart_detail.total = round(int(1)* course.price,2)
    cart_detail.save()
    return redirect(f'/courses/{course.slug}')



def remove_from_cart(request, id):
    cart_detail = CartDetial.objects.get(id=id)
    cart_detail.delete()
    return redirect('/orders/cart')



    
def cart(request):
    cart = get_object_or_404(Cart, user=request.user, status="InProgress")
    cart_detail = CartDetial.objects.filter(cart=cart)

    print(f"Request Method: {request.method}")  # Debugging statement
    print(f"GET Data: {request.GET}")  # Debugging statement

    if request.method == 'GET':
        coupon_code = request.GET.get('coupon_code')
        print(f"Coupon Code: {coupon_code}")  # Debugging statement

        if coupon_code:
            try:
                coupon = get_object_or_404(Coupon, code=coupon_code)
                print(f"Coupon: {coupon}")  # Debugging statement
                print(f"Coupon Quantity: {coupon.quantity}")  # Debugging statement
            except Coupon.DoesNotExist:
                return render(request, 'cart.html', {
                    'cart_detail': cart_detail,
                    'sub_total': cart.cart_total(),
                    'error': 'Invalid coupon code.'
                })

            if coupon and coupon.quantity > 0:
                today_date = datetime.datetime.today().date()

                if today_date >= coupon.start_date.date() and today_date <= coupon.end_date.date():
                    coupon_value = cart.cart_total() * coupon.discount / 100
                    cart_total = cart.cart_total() - coupon_value

                    coupon.quantity -= 1
                    coupon.save()

                    cart.coupon = coupon
                    cart.total_after_coupon = cart_total
                    cart.save()

                    cart = Cart.objects.get(user=request.user, status='InProgress')

                    return render(request, 'cart.html', {
                        'cart_detail': cart_detail,
                        'sub_total': cart.cart_total(),
                        'cart_total': cart_total,
                        'coupon_value': coupon_value,
                    })
                else:
                    return render(request, 'cart.html', {
                        'cart_detail': cart_detail,
                        'sub_total': cart.cart_total(),
                        'error': 'Coupon is not valid today.',
                    })
            else:
                return render(request, 'cart.html', {
                    'cart_detail': cart_detail,
                    'sub_total': cart.cart_total(),
                    'error': 'Coupon is no longer available.',
                })
        else:
            return render(request, 'cart.html', {
                'cart_detail': cart_detail,
                'sub_total': cart.cart_total(),
                'error': 'No coupon code provided.',
            })

    return render(request, 'cart.html', {
        'cart_detail': cart_detail,
        'sub_total': cart.cart_total(),
    })
                      











def checkout(request):
    return render (request, 'checkout.html')

