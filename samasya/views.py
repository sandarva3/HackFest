from django.shortcuts import render
from django.http import HttpResponse
def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return HttpResponse("About Page")


def login_view(request):
    return HttpResponse("Login Page")


def register_view(request):
    return HttpResponse("Register Page")


def post_view(request):
    return HttpResponse("Post Page")


def trending_view(request):
    return HttpResponse("Trending Page")