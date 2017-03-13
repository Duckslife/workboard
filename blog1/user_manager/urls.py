from django.conf.urls import  url

from user_manager.views import login, login_validate, join_page

urlpatterns=[
        
    url(r'^login/$', login, name= 'login'),
    url(r'^login/validate/$', login_validate, name= 'validate'),
    url(r'^join/$', join_page, name= 'userjoin'),        
        
]
