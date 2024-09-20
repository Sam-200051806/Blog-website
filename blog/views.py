from django.shortcuts import render,get_object_or_404
# from datetime import date
# Create your views here.
from .models import Post
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
    ip = Post.objects.get(slug = slug)
    return render(request,"blog/post-detail.html",{
        "post" : ip,
        "post_tags" : ip.tag.all()
    })