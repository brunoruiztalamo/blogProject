from django.shortcuts import render
from django.views import generic, View
from django.views.generic import ListView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileEditForm

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('miperfil')


class UserView(ListView):
    model = Profile
    template_name = 'autores.html'
    

class ProfileView(View):
    template_name = 'miperfil.html'
    
    def get(self, request, *args, **kwargs):
        user_profile = Profile.objects.get(user=request.user)  # Suponiendo que cada usuario tiene un perfil asociado
        context = {
            'user_profile': user_profile,
        }
        return render(request, self.template_name, context)