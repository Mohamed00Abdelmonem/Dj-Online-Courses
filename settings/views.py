from django.shortcuts import render
from .models import Company
from courses.models import Course, Review
from django.contrib.auth.models import User
def home(request):
    data = Company.objects.last()
    courses = Course.objects.all()[:5]
    reviews = Review.objects.all()[:5]
    users = User.objects.all()

    return render(request, 'home.html', {'data':data, 'courses':courses, 'reviews':reviews, "users":users})