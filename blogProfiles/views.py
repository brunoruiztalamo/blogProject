from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserRegisterForm, UserUpdateForm, UserProfileForm
from .models import UserProfile
from django.views import View

#Vista de Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            user = authenticate(request, first_name=first_name, last_name=last_name, username=username, password=password, email=email)

            if user is not None:
                login(request, user)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    
    return render(
       request=request,
       template_name='login.html',
       context={'form': form},
   )



class UserRegisterView(View):
    template_name = 'registro.html'
    form_class = UserRegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()  # Guarda usuario registrado
            
            # Creo el perfil asociado al usuario registrado
            user_profile = UserProfile.objects.create(user=new_user)
            
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')
        return render(request, self.template_name, {'form': form})




from django.contrib import messages

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserUpdateForm
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        return self.request.user.userprofile  # Obtén el UserProfile del usuario actual

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, 'Cambios guardados exitosamente.')
        else:
            messages.error(self.request, 'Hubo un error al guardar los cambios.')
        return super().form_valid(form)




class ProfileView(LoginRequiredMixin, View):
    template_name = 'miperfil.html'
    
    def get(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)  # Obtén el perfil del usuario actual
        return render(request, self.template_name, {'user_profile': user_profile})



#borrar usuario
class userDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    success_url = reverse_lazy('borrar_usuario.html')
    
    
    
#Vista de Logout
class CustomLogoutView(LoginRequiredMixin, LogoutView):
       template_name = 'logout.html'



#Mostrar todos los autores
@login_required(login_url='login')
def autores(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'autores.html', {'user_profiles': user_profiles})