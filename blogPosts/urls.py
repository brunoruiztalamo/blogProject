from django.urls import path
from .views import AddPostView, PostView, PostMain
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('postmain/', PostMain.as_view(), name="postmain"),
    path('crearPost/', AddPostView.as_view(), name="formulario_post"),
    path('detalle_post/<int:id>', PostView.as_view(), name='detalle_post'),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


