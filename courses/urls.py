from django.urls import path
from . import views
from .api import CourseList, CourseDetail
app_name = 'courses'

urlpatterns = [

    path('', views.Course_Grid.as_view()),
    path('notification', views.notifications, name='notification'),
    path('instractor-profile/<int:pk>', views.InstractorDetial.as_view(), name= 'instractor_profile'),
    path('list', views.CourseListView.as_view(), name='course_list'),
    path('course/<slug:course_slug>/quiz/<slug:slug>/', views.quiz, name='quiz'),
    path('<slug:slug>', views.Course_Detail.as_view(),name='course_detail'),
    path('<slug:slug>/add-review', views.add_review, name='add_review'),
    path('course/<slug:slug>/lessons/', views.LessonList.as_view()),
    path('course/<slug:course_slug>/lessons/<slug:slug>/', views.Lesson_Detail.as_view()),
    path('pdf_view_resource/<slug:slug>/', views.pdf_view_resources, name='pdf_view_resources'),
    path('pdf_view_slide/<slug:slug>/', views.pdf_view_slides, name='pdf_view_slides'),
    path('courses/filter/', views.filter_courses, name='filter_courses'),




    # api
    path('api/courses/', CourseList.as_view()),
    path('api/courses/<int:pk>', CourseDetail.as_view()),
]
