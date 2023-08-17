from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

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


#Form para crear los campos completos de usuario
class UserCustomForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, 
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    first_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')