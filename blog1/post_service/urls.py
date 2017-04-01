from django.conf.urls import url

from post_service.views import post_list, post_write_form

urlpatterns=[
    
    url(r'^$',post_list, name= 'list'),  
    url(r'write/', post_write_form, name='write_form'),
]




