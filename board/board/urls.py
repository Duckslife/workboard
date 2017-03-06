"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from workboard import views
from django.views.decorators.csrf import csrf_exempt 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name ='home'),
    url(r'^show_write_form/$',views.show_write_form, name='show_write_form'),
    url(r'^DoWriteBoard/$',views.DoWriteBoard, name ='DoWriteBoard'),
    url(r'^listSpecificPageWork/$',views.listSpecificPageWork, name = 'listSpecificPageWork'),
    url(r'^view_work/$', views.view_work, name='view_work'),
    url(r'^listSearchedSpecificPageWork/$',views.list_searched_specific_page_work, name='listsearchedspecific'),
    url(r'^listSpecificPageWork_to_update/$', views.list_specific_page_work_to_update, name='page_update' )
    ]
