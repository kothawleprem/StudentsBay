from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from posts.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    name=""
    email=""
    phone=""
    content = ""
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

    if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            pass
    else:
        contact = Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
        messages.success(request,'Thank You!! Message Sent.')
    return render(request,'home/home.html')

def search(request):
    query = request.GET['query']
    if len(query)>50:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request,"Please fill the form correctly!!")
    context = {
        'allPosts' : allPosts
    }
    return render(request,'home/search.html',context)

def register(request):
    return render(request,'home/register.html')

def handleregister(request):
    if request.method == 'POST':
        uname = request.POST['name']
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        college = request.POST['college']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(uname) > 10:
            messages.error(request,"Username should be under 10 Characters")
            return redirect("register")
        if password1 != password2:
           messages.error(request,"Password Do Not Match")
           return redirect("register") 
        
        ouruser = User.objects.create_user(uname,email,password1)
        ouruser.name = name
        ouruser.save()
        messages.success(request,"Account created!!!")
        return redirect('home')
    else:
        return HttpResponse('Not found')

def ulogin(request):
    return render(request,'home/login.html')

def handlelogin(request):
    if request.method == 'POST':
        loginuname = request.POST['loginuname']
        loginpassword = request.POST['loginpassword']
        print("In login")
        user = authenticate(username=loginuname,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"Invalid Credentials, Please try again!")
            return redirect('ulogin')
    print("Not POST")
    return HttpResponse('handlelogin')



def handlelogout(request):
    logout(request)
    return redirect('home')

    

