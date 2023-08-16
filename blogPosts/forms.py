from django import forms
from .models import Categoria, Post, Comentario
from django.contrib.auth.models import User


class formularioPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        fields = ['title', 'timestamp', 'content', 'image']
        labels = {
            'title': 'Título',
            'timestamp': 'Fecha y Hora',
            'content': 'Contenido',
            'image': 'Imagen',
        }


    
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comment']  # Asegúrate de que este campo coincide con el nombre en el modelo Comentario

    # Campo oculto para el ID del post comentado
    post_comentado = forms.IntegerField(widget=forms.HiddenInput())