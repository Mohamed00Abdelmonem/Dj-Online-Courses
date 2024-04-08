from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm, ActivateForm
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings    


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data['email']
           
            user = form.save(commit=False)
            user.is_active = False
            user.save()  

            profile = Profile.objects.get(user__username=username)

            send_mail(
                "Active you account ",
                f"Welcome {username} \n use this code {profile.code} to activate your account.",
                settings.EMAIL_HOST_USER,

                [email],
                fail_silently=False,
            )


            return redirect(f'/accounts/{username}/activate')
    
    else:
        form= SignupForm()

    return render(request, 'registration/signup.html', {'form': form})





def activate(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code:
                profile.code = ''


                user = User.objects.get(username=profile.user.username)
                user.is_active = True
                user.save()

                return redirect('/accounts/login')
    else:
        form = ActivateForm()

    return render(request,'registration/activate.html', {'form':form})        

