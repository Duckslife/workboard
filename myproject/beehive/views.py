from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request,'beehive/index.html',{
        'post_list':post_list
    })

def post_new(request):
    return render(request, 'beehive/post_form.html')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'behive/post_detail',{
        'post':post
    })

def base(request):
    return render(request, 'beehive/base.html')

def resume(request):
    return render(request, 'beehive/resume.html')

def portfolio(request):
    return render(request, 'beehive/portfolio-3-col.html')

def contacts(request):
    return render(request, 'beehive/contacts.html')

def feedback(request):
    return render(request, 'beehive/feedback.html')

def blog(request):
    post_list = Post.objects.all()
    return render(request, 'beehive/blog.html',{
        'post_list':post_list
    })
