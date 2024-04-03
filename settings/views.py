from django.shortcuts import render
from .models import Company


def home(request):
    data = Company.objects.last()

    return render(request, 'home.html', {'data':data})