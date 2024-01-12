from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Customer, User




def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'aboutus.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('home')
            return render(request, 'register.html', {'form':form})

        else:
            form = CustomUserCreationForm()
            return render(request, 'register.html', {'form': form})
    


def post_view(request):
    return render(request, 'post.html')


def profile_view(request):
    return render(request, 'profile.html')