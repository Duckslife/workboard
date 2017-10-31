from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',{
        'post_list':post_list
    })

def post_new(request):
    return render(request, 'blog/post_form.html')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail',{
        'post':post
    })

def another(request):
    return render(request, 'blog/another.html')

def myroute(request):
    return render(request, 'blog/myroute.html')

def write(request):
    return render(request, 'blog/write.html')

def signup(request):
    return render(request, 'blog/signup.html')


def base(request):
    return render(request, 'blog/base.html')

def resume(request):
    return render(request, 'blog/resume.html')

def portfolio(request):
    return render(request, 'blog/portfolio-3-col.html')

def contacts(request):
    return render(request, 'blog/contacts.html')

def feedback(request):
    return render(request, 'blog/feedback.html')


def blog(request):
    post_list = Post.objects.all()
    return render(request, 'blog/blog.html',{
        'post_list':post_list
    })
