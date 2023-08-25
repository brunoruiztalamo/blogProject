from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, default=None)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(default='#Título', max_length=100)
    header = models.CharField(default = '#subtítulo', max_length=100)
    timestamp = models.DateTimeField(default=timezone.now())
    content = models.TextField(default='#Contenido', max_length=10000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='#USER')
    image = models.ImageField(upload_to='posts/', default="#IMAGE")
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    
    def __str__(self):
        return f' {self.title} - Usuario: {self.user}'

    def get_absolute_url(self):
        return reverse('detalle_post', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()





# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, default='#POST', related_name="comments")
#     name = models.CharField(max_length=255)
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
