from django.shortcuts import render
from .models import Company
from courses.models import Course, Review

def home(request):
    data = Company.objects.last()
    courses = Course.objects.all()[:5]
    reviews = Review.objects.all()[:5]

    return render(request, 'home.html', {'data':data, 'courses':courses, 'reviews':reviews})