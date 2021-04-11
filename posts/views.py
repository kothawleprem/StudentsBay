from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post,PostComment

# Create your views here.
def postHome(request):
    allPosts = Post.objects.all().order_by('-sno')
    context = {
        'allPosts' : allPosts,
    }
    return render(request,'posts/postHome.html',context)

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.save()
    comments = PostComment.objects.filter(post=post).order_by('-sno')
    context = {
        'post' : post,
        'comments' : comments,
        'user' : request.user,
    }
    return render(request,'posts/post.html',context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        comment = PostComment(comment=comment,user=user,post=post)
        comment.save()
    return redirect(f'/posts/{post.slug}')

def emailme(request):
    if request.method == "POST":
        content = request.POST.get("uemail")
        # content = request.POST.get("value")
        print(content)
    return redirect(f'/posts')