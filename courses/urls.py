from django.urls import path

from .api import CategoryAPI, CoursesAPI, ReviewsAPI

urlpatterns = [
    
    path('categorys/', CategoryAPI.as_view()),
    path('courses/', CoursesAPI.as_view()),
    path('courses/<int:pk>', CoursesAPI.as_view()),
    path('reviews/', ReviewsAPI.as_view()),

]

