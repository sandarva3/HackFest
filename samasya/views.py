from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Customer



def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'aboutus.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password1')
            user = form.save(commit=True)
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                phone = form.cleaned_data.get('phone')
                Customer.objects.create(user=user, phone=phone)
                return redirect('home')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)
    


def post_view(request):
    return render(request, 'post.html')


def profile_view(request):
    return render(request, 'profile.html')