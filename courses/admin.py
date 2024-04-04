from django.contrib import admin
from .models import Course, Review, Lesson
# Register your models here.


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Review)