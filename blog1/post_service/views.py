from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from post_service.models import post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from post_service.forms import LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate
'''
1.8 django 
from django.core.context_processors import csrf
'''
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):

    template = get_template('login_form.html')
    context = Context({'login_form':LoginForm()})
   
    return HttpResponse(template.render(context, request))
    
@csrf_exempt
def login_validate(request):

    login_form_data = LoginForm(request.POST)
    
    if login_form_data.is_valid():
        
        user = auth.authenticate(username=login_form_data.cleaned_data['id'],password=login_form_data.cleaned_data['password'])
        print(user) 

        if user is not None:
            
            if user.is_active:
                
                auth.login(request,user)
                
                return redirect('/blog')
        else:
          
            return HttpResponse('user not find & pass miss')
    else:
        
        return HttpResponse('not login form')

    return HttpResponse('Not found error')

def post_list(request):
   
    template = get_template('post_list.html')
    page_data = Paginator(post.objects.all(), 5)
    page = request.GET.get('page')
    
    if page is None:
        
        page = 1

    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)
    
    context = Context({'post_list':posts, 'current_page':int(page), 'total_page':range(1, page_data.num_pages + 1)})
    return HttpResponse(template.render(context))
