from django.contrib import admin
from .models import Entries,Categories,TagModel
# Register your models here.
admin.site.register(Entries)

admin.site.register(Categories)

admin.site.register(TagModel)
