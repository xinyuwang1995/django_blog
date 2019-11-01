from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=80,blank=True)
    subtitle = models.CharField(max_length=80,blank=True)
    publish_date = models.DateTimeField(auto_now_add=True,blank=True)
    content = models.TextField(blank=True,default='')
    link = models.CharField(max_length=100,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    tag = models.ManyToManyField(Tag,blank=True,default='')

    def __str__(self):
        return self.title

