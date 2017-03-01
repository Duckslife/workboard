# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entries

def index(request,page = 1):
    per_page = 5
    start_pos = (page -1)* per_page
    end_pos = start_pos + per_page

    page_title = 'blog list views'
    
    entries = Entries.objects.all().order_by('-created')[start_pos:end_pos]
    print(entries[0].Title.encode('utf-8'))
    return HttpResponse('hello worlds %s', entries[0].Title.encode('utf-8'))


def read(request, entry_id=None):
    
    page_title = 'read page'

    return HttpResponse('hello %s $d ',[page_title,int(entry_id)])
