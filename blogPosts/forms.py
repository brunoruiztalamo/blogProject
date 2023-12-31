from django import forms
from .models import  Post

class formularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'header','category', 'timestamp', 'content', 'image']
        labels = {
            'title': 'Título',
            'header': 'Encabezado',
            'category': 'Categoria',
            'timestamp': 'Fecha y Hora',
            'content': 'Contenido',
            'image': 'Imagen',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
            'header': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'timestamp': forms.DateInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 200px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        
      
      
        
class formularioEdicion(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        fields = ['title', 'timestamp', 'content', 'image']
        labels = {
            'title': 'Título',
            'timestamp': 'Fecha y Hora de Publicación',
            'content': 'Contenido',
            'image': 'Imagen',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


    
