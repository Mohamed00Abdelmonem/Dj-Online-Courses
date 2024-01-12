from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Courses(models.Model):
    name = models.CharField(max_length=20)
    sub_title = models.TextField(max_length=1000)
    description= models.TextField(max_length=2500)
    image = models.ImageField(upload_to='course_cover_image', null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='category_course', on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Courses, related_name='courses_review', on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} writing review {self.review[0:50]} for course {self.course}'
    