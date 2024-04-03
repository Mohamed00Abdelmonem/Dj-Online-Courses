from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Course, Review
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
