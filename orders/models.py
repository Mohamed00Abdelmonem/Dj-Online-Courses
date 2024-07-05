from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


CART_STATUS = {
    ('InProgress','InProgress'),
    ('Completed','Completed'),
}

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.SET_NULL,null=True, blank=True)
    status = models.CharField(choices=CART_STATUS, max_length=20)

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        else:
            return f"Cart (No User)"


class CartDetial(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_detail')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True , blank=True, related_name='courses_in_cart')

    def __str__(self) -> str:
        if self.cart:
            return f"cart_detail {self.cart}"
        else: 
            return f"Cart (no user)"