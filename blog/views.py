from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blogProfiles.models import UserProfile
from django.views import View
from django.utils.decorators import method_decorator


@login_required(login_url='login') 
def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='about.html',
        context=contexto,
    )
    return http_response



class InicioView(View):
    template_name = 'inicio.html'
    
    @method_decorator(login_required(login_url='login'))
    def get(self, request, *args, **kwargs):
        user_profile = None
        avatar_url = None

        try:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile.avatar:
                avatar_url = user_profile.avatar.url
        except UserProfile.DoesNotExist:
            user_profile = None

        context = {'user_profile': user_profile, 'avatar_url': avatar_url}
        return render(request, self.template_name, context)

