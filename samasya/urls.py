from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutus/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('post/', views.post_view, name='post'),
    path('profile/', views.profile_view, name ='profile'),
]
