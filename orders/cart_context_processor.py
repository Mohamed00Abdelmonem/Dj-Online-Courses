from .models import Cart, CartDetial


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, status='InProgress')
        if not created:
            cart_detail = CartDetial.objects.filter(cart=cart)
            return {'cart_data': cart, 'cart_detail_data':cart_detail}
        return {'cart_data':cart}

    else:
        return {}    