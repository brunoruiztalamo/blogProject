from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from blogPosts.models import Post

def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='about.html',
        context=contexto,
    )
    return http_response



class InicioView(ListView):
    model = Post
    template_name = 'inicio.html'

