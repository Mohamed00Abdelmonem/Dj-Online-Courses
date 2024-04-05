from django.shortcuts import render
from .models import Company
from courses.models import Course

def home(request):
    data = Company.objects.last()
    courses = Course.objects.all()[:5]

    return render(request, 'home.html', {'data':data, 'courses':courses})