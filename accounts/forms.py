from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Instructor_Profile



class SignupForm(UserCreationForm):
    # username = 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
