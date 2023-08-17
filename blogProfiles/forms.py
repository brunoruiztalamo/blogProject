from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    model = Profile
    fields = ['user', 'bio', 'email', 'avatar']
    labels = {
        
        'user': 'Usuario',
        'bio':'Bio',
        'email':'Email',
        'avatar':'Avatar'   
    }   
    widgets = {
    'user': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
    'bio': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
    'email': forms.EmailField(),
    'Avatar': forms.FileInput(attrs={'class': 'form-control'}),
    
    }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'email', 'avatar']
        labels = {
            
            'bio':'Bio',
            'email':'Email',
            'avatar':'Avatar'   
        }   
        widgets = {
            
        'bio': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
        #'email': forms.EmailField(),
        'Avatar': forms.FileInput(attrs={'class': 'form-control'}),
        
        }


