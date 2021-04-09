from django.shortcuts import render,HttpResponse

# Create your views here.
def postHome(request):
    return render(request,'posts/postHome.html')

def post(request, slug):
    context = {
        'slug' : slug,
    }
    return render(request,'posts/post.html',context)