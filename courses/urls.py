from django.urls import path
from .views import Course_Grid, Course_List, Course_Detail, LessonList, Lesson_Detail, add_review


app_name = 'courses'

urlpatterns = [
    path('', Course_Grid.as_view()),
    path('list', Course_List.as_view()),
    path('<int:pk>', Course_Detail.as_view()),
    path('<int:id_course>/add-review', add_review, name='add_review'),

    path('course/<int:course_pk>/lessons/', LessonList.as_view()),  # Changed the named group to course_pk and added trailing slash
    path('course/<int:course_pk>/lessons/<int:pk>/', Lesson_Detail.as_view()),  # Changed the named group to course_pk
    path('course/<int:course_pk>/lessons/<int:pk>/', Lesson_Detail.as_view()),  # Changed the named group to course_pk
]
