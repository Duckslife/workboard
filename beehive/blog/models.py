from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Trip_master(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    public_yn = models.CharField(max_length=1)
    start_dt = models.CharField(max_length=14)
    end_dt = models.CharField(max_length=14)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Trip_day(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Trip_schedule(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=32, null=False)

    content = models.TextField(max_length=1000)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
