from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from blogPosts.models import Post

@login_required(login_url='login') 
def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='about.html',
        context=contexto,
    )
    return http_response



def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

