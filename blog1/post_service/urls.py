from django.conf.urls import url

from post_service.views import post_list, login

urlpatterns=[
    
    url(r'^$',post_list, name= 'list'),            
    url(r'^login/', login, name= 'login')       
]




