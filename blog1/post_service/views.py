from django.shortcuts import render, redirect, render_to_response

from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from post_service.models import post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
'''
1.8 django 
from django.core.context_processors import csrf
'''



def post_list(request):

    is_login=request.session.get('is_login',False)
    
    if is_login == 'ok':
       
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
    else:
        return HttpResponse('plz login')


def post_write_form(request):
    
    
    return HttpRespons(e'write_form.html')

