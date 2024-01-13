from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CustomUserCreationForm, PostForm, CommentForm
from django.contrib import auth
from django.contrib.auth import login, logout
from .models import Customer, User, Post, Comment
from django.contrib.auth.decorators import login_required


def home_view(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('-created_at')
    
        comment_form = CommentForm()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                post_id = request.POST.get('post_id')
                comment.post = Post.objects.get(id=post_id)
                comment.save()
                return redirect('home')

        comments = Comment.objects.all().order_by('-created_at')
        context = {
            'posts':posts,
            'comments':comments,
            'comment_form':comment_form,
            }
        return render(request, 'home.html', context)
    
    return render(request, 'notloginhome.html')


def about_view(request):
    return render(request, 'aboutus.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


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
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            form = PostForm()

    return render(request, 'post.html', {'form': form})


def comment_view(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        text = request.POST.get('text')
        post = get_object_or_404(Post, id=post_id)

        Comment.objects.create(user=request.user, post=post, text=text)

        return redirect('home')
    
    return redirect('home')

def profile_view(request):
    if request.user.is_authenticated:
        user_posts = Post.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'profile.html', {'posts':user_posts})
    return render(request, 'profile.html')