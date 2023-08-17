from django.urls import path
from .views import UserRegisterView, UserProfileView, UserView, UserDeleteView, ProfileUpdateView, ProfileView, UserLogoutView


urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name='registro'),
    path('autores/', UserView.as_view(), name='autores'),
    path('editar-perfil/<int:pk>/', ProfileUpdateView.as_view(), name='editar_perfil'),
    path('miperfil/', ProfileView.as_view(), name='miperfil'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('borrar_usuario/<int:pk>', UserDeleteView.as_view(), name='borrar_usuario'),
    path('ver_perfil/<int:pk>', UserProfileView.as_view(), name='ver_perfil' )

]

