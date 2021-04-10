from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post,PostComment

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
    post.views = post.views + 1
    post.save()
    comments = PostComment.objects.filter(post=post)
    print(request.user)
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