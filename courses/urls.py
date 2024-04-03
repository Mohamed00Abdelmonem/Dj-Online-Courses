from django.urls import path
from .views import Course_Grid, Course_List

urlpatterns = [
    path('', Course_Grid.as_view()),
    path('/list', Course_List.as_view()),
]