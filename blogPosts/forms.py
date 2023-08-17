from django import forms
from .models import Categoria, Post, Comentario
from django.contrib.auth.models import User


class formularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'header', 'timestamp', 'content', 'image']
        labels = {
            'user': 'Autor',
            'title': 'Título',
            'header': 'Encabezado',
            'timestamp': 'Fecha y Hora',
            'content': 'Contenido',
            'image': 'Imagen',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
            'header': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight: bold;'}),
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


    
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comment']  # Asegúrate de que este campo coincide con el nombre en el modelo Comentario

    # Campo oculto para el ID del post comentado
    post_comentado = forms.IntegerField(widget=forms.HiddenInput())