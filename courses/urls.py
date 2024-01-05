from django.urls import path

from .api import CategoryAPI, CategoryDetailAPI, CoursesAPI, CoursesDetailAPI, ReviewsAPI

urlpatterns = [
                                                                
    path('categorys/', CategoryAPI.as_view()),
    path('categorys/<int:pk>', CategoryDetailAPI.as_view()),
    path('courses/', CoursesAPI.as_view()),
    path('courses/<int:pk>', CoursesDetailAPI.as_view()),
    path('reviews/', ReviewsAPI.as_view()),

]

