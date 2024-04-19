from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [

    path('', views.Course_Grid.as_view()),
    path('list', views.Course_List.as_view()),
    path('course/<slug:course_slug>/quiz/<slug:slug>/', views.quiz, name='quiz'),
    path('<slug:slug>', views.Course_Detail.as_view()),
    path('<slug:slug>/add-review', views.add_review, name='add_review'),
    path('course/<slug:slug>/lessons/', views.LessonList.as_view()),
    path('course/<slug:course_slug>/lessons/<slug:slug>/', views.Lesson_Detail.as_view()),
    path('pdf_view_resource/<slug:slug>/', views.pdf_view_resources, name='pdf_view_resources'),
    path('pdf_view_slide/<slug:slug>/', views.pdf_view_slides, name='pdf_view_slides'),

]
