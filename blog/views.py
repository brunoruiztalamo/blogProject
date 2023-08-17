from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from blogPosts.models import Post
from blogProfiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


#Vista de la pagina About
class AboutView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
            profile = Profile.objects.get(user=request.user)
            context = {'profile': profile}
            return render(request, self.template_name, context)


#Vista de pag inicio
class InicioView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'inicio.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el perfil del usuario logueado
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        
        return context
