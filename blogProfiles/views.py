from django.shortcuts import render
from django.views import generic, View
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileEditForm, UserCustomForm
from django.contrib.auth.models import User



#Crear Usuario
class UserRegisterView(generic.CreateView):
    form_class = UserCustomForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        #login(self.request, self.object)
        
        Profile.objects.create(user=self.object)
        
        return response
    


#Log Out
class UserLogoutView(LogoutView):
    template_name = 'logout.html'



#Editar datos
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'editar_perfil.html'

    def get_success_url(self):
        return reverse_lazy('editar_perfil', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        # Obtener el perfil del usuario o crear uno si no existe
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    
    
#Ver perfiles/autores
class UserView(ListView):
    model = Profile
    template_name = 'autores.html'
    context_object_name = 'autores'

    def get_queryset(self):
        return Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context
    
    

#Ver mi perfil
class ProfileView(View):
    template_name = 'miperfil.html'
    
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        context = {'profile': profile}
        return render(request, self.template_name, context)


class UserProfileView(DetailView):
    model = User
    template_name = 'ver_perfil.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = self.get_object()
        context['profile'] = Profile.objects.get(user=profile_user)
        
        # Obtener la URL de la página anterior
        context['previous_page'] = self.request.META.get('HTTP_REFERER')
        return context

#borrar usuario
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User  # Cambia el modelo a User
    template_name = 'borrar_usuario.html'
    success_url = reverse_lazy('inicio')

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        
        # Borra el perfil asociado al usuario
        profile = user.profile
        if profile:
            profile.delete()

        user.delete()
        return super().delete(request, *args, **kwargs)



