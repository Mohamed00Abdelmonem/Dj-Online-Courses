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


class Course_Detial(DetailView):
    model = Course
    template_name = 'course-details.html'

