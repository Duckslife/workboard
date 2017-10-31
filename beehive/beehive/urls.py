"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^index', index, name='index'),
    url(r'^signup/$', signup ,name='signup'),
    url(r'^another/$', another ,name='another'),
    url(r'^myroute/$', myroute ,name='myroute'),
    url(r'^write/route$', write ,name='write'),
    #url(r'^resume/', resume, name='resume'),
    #url(r'^portfolio/$', portfolio ,name='portfolio'),
    #url(r'^contacts/$', contacts ,name='contacts'),
    #url(r'^feedback/$', feedback ,name='feedback'),
    #url(r'^blog/$', blog ,name='blog'),

    url(r'^new/$', post_new ,name='post_new'),
    url(r'^blog/(?P<pk>\d+)/$', post_detail ,name='post_detail'),

]
