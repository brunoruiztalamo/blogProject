from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class Post(models.Model):
    title = models.CharField(default='#Título', max_length=100)
    header = models.CharField(default = '#subtítulo', max_length=100)
    timestamp = models.DateTimeField(default=timezone.now())
    content = models.TextField(default='#Contenido', max_length=10000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='#USER')
    image = models.ImageField(upload_to='posts/', default="#IMAGE")
    
    def __str__(self):
        return f' {self.title} - Usuario: {self.user}'

    def get_absolute_url(self):
        return reverse('detalle_post', kwargs={'pk': self.pk})
    


