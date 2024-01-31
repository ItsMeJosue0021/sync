from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, PostImage

#=========================================================
# Home Page
#=========================================================

def home(request):
    return render(request, 'pages/home.html')

#=========================================================
# About Page
#=========================================================

def about(request):
    return render(request, 'pages/about.html')

#=========================================================
# Login Page
#=========================================================

def login(request):
    return render(request, 'pages/login.html')

#=========================================================
# Register Page
#=========================================================

def register(request):
    return render(request, 'pages/register.html')   

#=========================================================
# Feed Page
#=========================================================

def feed(request):
    posts = Post.objects.all()
    return render(request, 'pages/feed.html', {'posts': posts})
    # return render(request, 'pages/feed.html')

#=========================================================
# Profile Page
#=========================================================

def profile(request):
    return render(request, 'pages/profile.html')

#=========================================================
# Create Post
#=========================================================

def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            post = form.save()    
            handle_image_uploads(request, post)
            return redirect('create_post')
    else:
        form = PostForm()

    return render(request, 'pages/post/create.html', {'form': form})

#=========================================================
# Edit Post
#=========================================================

def editPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            handle_image_uploads(request, post)
            return redirect('edit_post', post_id=post.id)  
    else:
        form = PostForm(instance=post)

    return render(request, 'pages/post/edit.html', {'form': form, 'post': post})

#=========================================================
# Handle Multple Image Upload
#=========================================================

def handle_image_uploads(request, post):
    for image_file in request.FILES.getlist('images'):
        PostImage.objects.create(post=post, file=image_file)

#=========================================================
# Delet Post
#=========================================================

def deletePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('feed')
