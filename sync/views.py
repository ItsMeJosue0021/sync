from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')   

def feed(request):
    return render(request, 'pages/feed.html')

def profile(request):
    return render(request, 'pages/profile.html')

