from django.conf.urls import url

from post_service.views import post_list, login, login_validate

urlpatterns=[
    
    url(r'^$',post_list, name= 'list'),            
    url(r'^login/$', login, name= 'login'),
    url(r'login/validate/$',login_validate, name='validate')
]




