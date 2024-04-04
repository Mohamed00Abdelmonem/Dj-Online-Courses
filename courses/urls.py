from django.urls import path
from .views import Course_Grid, Course_List, Course_Detail, LessonList, Lesson_Detail


app_name = 'courses'

urlpatterns = [
    path('', Course_Grid.as_view()),
    path('list', Course_List.as_view()),
    path('<int:pk>', Course_Detail.as_view()),
    path('course/<int:course_pk>/lessons/', LessonList.as_view()),  # Changed the named group to course_pk and added trailing slash
    path('course/<int:course_pk>/lessons/<int:pk>/', Lesson_Detail.as_view()),  # Changed the named group to course_pk
]
