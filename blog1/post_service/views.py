from django.shortcuts import render

from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template

def post_list(request):
   
    template = get_template('post_list.html')
    context = Context({})

    return HttpResponse(template.render(context))
