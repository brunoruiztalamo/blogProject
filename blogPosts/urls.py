from django.urls import path
from .views import AddPostView, PostView, PostMain, PostUpdateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostMain.as_view(), name="postmain"),
    path('crearPost/', AddPostView.as_view(), name="formulario_post"),
    path('detalle_post/<int:pk>', PostView.as_view(), name='detalle_post'),
    path('detalle_post/editar/<int:pk>', PostUpdateView.as_view(), name='editar_post')
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


