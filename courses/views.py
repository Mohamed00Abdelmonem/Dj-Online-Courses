from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Course, Review, Lesson, Unit
from django.views.generic import ListView, DetailView
from django.urls import reverse


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
    # slug_url_kwarg = 'slug'  # specify the slug URL keyword


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_course = self.get_object()
        # current_lessons = Lesson.objects.filter(course =current_course)
        related_unit = Unit.objects.filter(Course=current_course )
          # Create a dictionary to store units and their corresponding lessons
        unit_lessons = {}

        # Iterate over each unit and retrieve its associated lessons
        for unit in related_unit:
            unit_lessons[unit] = unit.lesson_unit.all()

        related_courses = Course.objects.filter(tags__in=current_course.tags.all()).exclude(id=current_course.id).distinct()
        context["related_courses"] = related_courses
        context["related_unit"] = related_unit
        context["unit_lessons"] = unit_lessons
        # context["current_lessons"] = current_lessons
        context["current_course"] = current_course


        return context
    


def add_review(request, slug):
        course = Course.objects.get(slug=slug)
        rate = request.POST['rate']
        review = request.POST['review']
        
        Review.objects.create(
            course=course,
            rate=rate,
            comment=review,
            user=request.user
        )

        return redirect(f'/courses/{course.slug}')










class LessonList(ListView):
    model = Lesson
    template_name = 'lesson-list.html'
    context_object_name = 'lessons'


    def get_queryset(self):
        course = Course.objects.get(id=self.kwargs['course_pk']) # this inectance course
        queryset_lessons = Lesson.objects.filter(course=course)
        return queryset_lessons







class Lesson_Detail(DetailView):
    model = Lesson
    template_name = 'lesson-details.html' 

