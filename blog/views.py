from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from blogPosts.models import Post
from blogProfiles.models import Profile
from django.shortcuts import get_object_or_404



#Vista de la pagina About
class AboutView(View):
    template_name = 'about.html'

    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            context = {'profile': profile}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)


class InicioView(ListView):
    template_name = 'inicio.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Filtra los perfiles asociados al usuario actual
            profiles = Profile.objects.filter(user=request.user)
            
            if profiles.exists():
                # Si existen perfiles, toma el primero (puedes ajustar la lógica si hay más de uno)
                profile = profiles.first()
            else:
                # Si no hay perfiles, puedes crear uno aquí si es necesario
                profile = Profile.objects.create(user=request.user)
                
            context = {'profile': profile}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)