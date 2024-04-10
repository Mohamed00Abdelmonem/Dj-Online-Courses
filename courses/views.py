from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
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
        current_lessons = Lesson.objects.filter(course =current_course )
        related_courses = Course.objects.filter(tags__in=current_course.tags.all()).exclude(id=current_course.id).distinct()
        context["related_courses"] = related_courses
        context["current_lessons"] = current_lessons
        context["current_course"] = current_course


        return context
    

def add_review(request, id_course):
        course = Course.objects.get(id= id_course)
        rate = request.POST['rate']
        review = request.POST['review']

        Review.objects.create(
            course = course,
            rate = rate,
            comment = review,
            user = request.user
        )

        # new reviews
        # reviews = Review.objects.filter(product=product)
        # html = render_to_string('include/reviews_include.html', {'reviews':reviews})
        # return JsonResponse({'result':html})

        return redirect(f'/courses/{course.id}')

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
