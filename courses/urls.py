from django.urls import path
from .views import Course_Grid, Course_List, Course_Detail, LessonList


app_name = 'courses'

urlpatterns = [
    path('', Course_Grid.as_view()),
    path('list', Course_List.as_view()),
    path('<int:pk>', Course_Detail.as_view()),
    path('course/<int:pk>/lessons', LessonList.as_view()),
]