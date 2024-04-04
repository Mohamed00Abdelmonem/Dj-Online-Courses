from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Course, Review, Lesson
from django.views.generic import ListView, DetailView


class Course_Grid(ListView):
    model = Course
    template_name = 'course-grid.html'
    context_object_name = 'courses'




class Course_List(ListView):
    model = Course
    template_name = 'course-list.html'
    context_object_name = 'courses'


class Course_Detail(DetailView):
    model = Course
    template_name = 'course-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_course = self.get_object()
        related_courses = Course.objects.filter(tags__in=current_course.tags.all()).exclude(id=current_course.id).distinct()
        context["related_courses"] = related_courses
        return context

from django.views.generic import ListView
from .models import Lesson, Course

class LessonList(ListView):
    model = Lesson
    template_name = 'lesson-list.html'
    context_object_name = 'lessons'


    def get_queryset(self):
        course = Course.objects.get(id=self.kwargs['pk']) # this inectance course
        queryset_lessons = Lesson.objects.filter(course=course)
        return queryset_lessons

