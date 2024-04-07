from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form= SignupForm()

    return render(request, 'registration/signup.html', {'form': form})

