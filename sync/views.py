from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, PostImage

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')   

def feed(request):
    posts = Post.objects.all()
    return render(request, 'pages/feed.html', {'posts': posts})
    # return render(request, 'pages/feed.html')

def profile(request):
    return render(request, 'pages/profile.html')

def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            post = form.save()
            
            handle_image_uploads(request, post)
            # Handle multiple file uploads using request.FILES.getlist
            # for image_file in request.FILES.getlist('images'):
            #     PostImage.objects.create(post=post, file=image_file)

            return redirect('create_post')  # Redirect to a view that displays the list of posts
    else:
        form = PostForm()

    return render(request, 'pages/post/create.html', {'form': form})

def editPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            handle_image_uploads(request, post)
            return redirect('post_list')  # Redirect to a view that displays the list of posts
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

def handle_image_uploads(request, post):
    for image_file in request.FILES.getlist('images'):
        PostImage.objects.create(post=post, file=image_file)
