from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class post(models.Model):
    
    title = models.CharField(max_length= 1024)
    body = models.CharField(max_length= 4096)
    author = models.ForeignKey(User)
    regdate = models.DateTimeField(auto_created= True, auto_now_add= True)

