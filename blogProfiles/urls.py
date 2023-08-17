from django.urls import path
from .views import UserRegisterView, UserView, ProfileUpdateView, ProfileView


urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name='registro'),
    path('autores/', UserView.as_view(), name='autores'),
    path('editar_perfil', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('miperfil/', ProfileView.as_view(), name="miperfil")

] 

