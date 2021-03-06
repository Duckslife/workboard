from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from user_manager.forms import LoginForm, join_form
from django.contrib.auth import authenticate
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


# Create your views here.
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
                request.session['is_login']='ok'
                return redirect('/blog/')
        else:
          
            return HttpResponse('user not find & pass miss')
    else:
        
        return HttpResponse('not login form')

    return HttpResponse('Not found error')



def join_page(request):
    
    if request.method == 'POST':
        
        form_data = join_form(request.POST)
        
        if form_data.is_valid():

            username = form_data.cleaned_data['id']

            password = form_data.cleaned_data['password']

            User.objects.create_user(username= username, password= password)

            return redirect('/user/login/')

    else:

        form_data = join_form()
    
    template = get_template('join_page.html')

    context = Context({'join_form': form_data})

    return HttpResponse(template.render(context, request))

