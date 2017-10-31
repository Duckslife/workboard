from django.contrib import admin
from .models import Post,Trip_schedule,Trip_master,Trip_day,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Post,PostAdmin)

class TripAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Trip_master,TripAdmin)

class TripdayAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Trip_day,TripdayAdmin)


class TripscheduleAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Trip_schedule,TripscheduleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content')

admin.site.register(Comment,CommentAdmin)
