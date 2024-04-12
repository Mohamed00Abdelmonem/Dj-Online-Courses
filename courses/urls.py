from django.urls import path
from .views import Course_Grid, Course_List, Course_Detail, LessonList, Lesson_Detail, add_review

app_name = 'courses'

urlpatterns = [
    path('', Course_Grid.as_view()),
    path('list', Course_List.as_view()),
    path('<slug:slug>', Course_Detail.as_view()),
    path('<slug:slug>/add-review', add_review, name='add_review'),
    path('course/<slug:slug>/lessons/', LessonList.as_view()),
    path('course/<slug:course_slug>/lessons/<slug:slug>/', Lesson_Detail.as_view()),
]
