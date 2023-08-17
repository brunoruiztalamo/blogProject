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
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            context = {'profile': profile}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)


#Vista de pag inicio
class InicioView(ListView):
    model = Post
    template_name = 'inicio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
