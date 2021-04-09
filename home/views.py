from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,'Please fill the form correctly. Note -> Minimum Characters: Name-2,Email-3,Phone-10,Message-4')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Thank You!! Message Sent.')

    return render(request,'home/about.html')