from django.shortcuts import render
from .models import Company
from courses.models import Course, Review
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from langchain_community.llms import Ollama




def home(request):
    data = Company.objects.last()
    courses = Course.objects.all()[:5]
    reviews = Review.objects.all()[:5]
    users = User.objects.all()

    return render(request, 'home.html', {'data':data, 'courses':courses, 'reviews':reviews, "users":users})





def generate_ollama3_text(request):
    generated_text = None
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  
        llm = Ollama(model="llama3")
        generated_text = llm.invoke(input_text)

    return render(request, 'ollama3_generator.html', {'generated_text': generated_text})
