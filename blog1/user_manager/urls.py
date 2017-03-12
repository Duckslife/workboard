from django.conf.urls import  url

from user_manager.views import login, login_validate

urlpatterns=[
        
    url(r'^login/$', login, name= 'login'),
    url(r'^login/validate/$', login_validate, name= 'validate'),
        
        
]
