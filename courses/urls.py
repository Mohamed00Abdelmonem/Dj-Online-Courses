from django.urls import path

from .api import CategoryAPI, CategoryDetailAPI, CoursesAPI, ReviewsAPI

urlpatterns = [
    
    path('categorys/', CategoryAPI.as_view()),
    path('categorys/<int:pk>', CategoryDetailAPI.as_view()),
    path('courses/', CoursesAPI.as_view()),
    path('courses/<int:pk>', CoursesAPI.as_view()),
    path('reviews/', ReviewsAPI.as_view()),

]

