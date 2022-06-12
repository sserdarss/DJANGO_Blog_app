from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, login 
from .forms import  RegisterForm,ProfileForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    # messages.success(request, 'You logged out!')
    logout(request)
    return render(request, 'users/logout.html')

def register(request):
    form_user = RegisterForm()

    if request.method == 'POST':
        form_user = RegisterForm(request.POST, request.FILES)

        if form_user.is_valid() :
            user = form_user.save()

            login(request, user)
            messages.success(request, 'Register Successfull!')

            return redirect('home')

    context = {
        "form_user": form_user,
    }

    return render(request, 'users/register.html',context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request,'login successfull')
            login(request, user)
            return redirect('home')

    return render(request, 'users/user_login.html', {"form":form})


def profile(request, id):
    user_profile = User.objects.get(id=id)
    form_profile = ProfileForm(instance=user_profile)


    if request.method == "POST" :
        form_profile = ProfileForm(request.POST,instance=user_profile)

       
        

        if form_profile.is_valid():
            user = form_profile.save()
            login(request,user)
            return redirect("home")
    context = {
        "form_profile": form_profile,
        "user_profile" : user_profile,
    }

    return render(request, 'users/profile.html',context)