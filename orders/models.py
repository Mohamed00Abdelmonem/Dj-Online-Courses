from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from utils.generate_code import generate_code
from django.utils import timezone
import datetime





CART_STATUS = {
    ('InProgress','InProgress'),
    ('Completed','Completed'),
}

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.SET_NULL,null=True, blank=True)
    status = models.CharField(choices=CART_STATUS, max_length=20)
    coupon = models.ForeignKey('Coupon', related_name='cart_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_after_coupon = models.FloatField(null=True,blank=True)
    
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
        


ORDER_STATUS = {
    ("InProgress","InProgress"),
    ("Completed", "Completed")
}

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_order')
    code = models.CharField(max_length=9 ,default=generate_code())
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default="InProgress")
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_after_coupon = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.user}'
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_detail")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='order_course', null=True, blank=True)
    price = models.FloatField()
    # total = models.FloatField(null=True, blank=True)
    
    def __str__(self):
            return f'{self.order}'




class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField()
    quantity= models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.code}'

    def save(self, *args, **kwargs):
      week = datetime.timedelta(days=7)
      self.end_date = self.start_date + week
      super (Coupon, self).save(*args, **kwargs)