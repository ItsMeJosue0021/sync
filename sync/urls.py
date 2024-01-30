from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),

    path('feed/', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),


    #=========================================================
    # Post
    #=========================================================
    path('post/new/', views.createPost, name='create_post'),
    # path('post/<int:pk>/', views.postDetail, name='post_detail'),

]