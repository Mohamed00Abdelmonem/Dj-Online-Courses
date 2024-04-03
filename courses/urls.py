from django.urls import path
from .views import Course_Grid, Course_List, Course_Detial

urlpatterns = [
    path('', Course_Grid.as_view()),
    path('/list', Course_List.as_view()),
    path('/<int:pk>', Course_Detial.as_view()),
]