from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, ProfileView, autores, CustomLogoutView, UserRegisterView, UserUpdateView, userDeleteView

urlpatterns = [
    path('registro/', UserRegisterView.as_view(), name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('editar_perfil/', UserUpdateView.as_view(), name="editar_perfil"),
    path('borrar_usuario/', userDeleteView.as_view(), name='borrar_usuario'),
    path('autores/', autores, name="autores"),
    path('miperfil/', ProfileView.as_view(), name="miperfil")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

