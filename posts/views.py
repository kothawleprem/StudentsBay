from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Post

# Create your views here.
def postHome(request):
    allPosts = Post.objects.all()
    context = {
        'allPosts' : allPosts,
    }
    print(allPosts)
    return render(request,'posts/postHome.html',context)

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    print(post)
    context = {
        'post' : post,
    }
    return render(request,'posts/post.html',context)
