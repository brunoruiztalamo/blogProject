from django.db import models
from django.contrib.auth.models import User
       

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="#USER")
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', default="#NOAVATAR")
    
    def __str__(self):
        return f'{self.user} - Profile'
