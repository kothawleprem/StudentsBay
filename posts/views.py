from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post,PostComment
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def postHome(request):
    allPosts = Post.objects.all().order_by('-sno')

    context = {
        'allPosts' : allPosts,
    }
    return render(request,'posts/postHome.html',context)

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    global postcontent
    global posttitle
    postcontent = post.content
    posttitle = post.title
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
        uemail = request.POST.get("uemail")
        # content = request.POST.get("value")
        print(uemail)
        print(postcontent)
        print(posttitle)
        subject, from_email, to = 'Your Post From StudentsBay has Arrived!!!', settings.EMAIL_HOST_USER,uemail
        text_content = 'Chart Sent Successfully'
        html_content = f"<center><h1>{posttitle}</h1></center>{postcontent}"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    return redirect(f'/posts')