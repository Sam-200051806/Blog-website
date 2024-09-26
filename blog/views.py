from django.shortcuts import render,get_object_or_404,redirect
# from datetime import date
# Create your views here.
from .models import Post ,Comments
from .forms import CommentForm

all_posts = [
   
]

def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts" : latest_post
    })
def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{
        "all_posts" : posts
    })
def post_details(request,slug):
    post = get_object_or_404(Post, slug=slug)
    ip = Post.objects.get(slug = slug)
    # comment = Comments.objects.get(slug = slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Create a comment instance but don't save it yet
            comment.posts = post  # Set the foreign key to the current post
            comment.save()  # Now save the comment
            return redirect('post-detail-page', slug=slug)  # Redirect to the same post
    else:
        form = CommentForm()  # Create a new empty form
    return render(request,"blog/post-detail.html",{
        "post" : ip,
        "post_tags" : ip.tag.all(),
        "form" : form
    })

def contact_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # return redirect('success')  # Redirect after successful submission
    else:
        form = CommentForm()  # Display an empty form

    return render(request , {'form': form})