from django.shortcuts import render
from django.http import HttpResponse
def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about-us.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')


def post_view(request):
    return render(request, 'post.html')


def profile_view(request):
    return render(request, 'profile.html')