from django.urls import path
from .views import AddPostView, PostListView, PostView, PostMain, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', PostMain.as_view(), name="postmain"),
    path('crearPost/', AddPostView.as_view(), name="formulario_post"),
    path('detalle_post/editar/<int:pk>', PostUpdateView.as_view(), name='editar_post'),
    path('detalle_posts/', PostListView.as_view(), name='detalle_posts'),
    path('detalle_post/detalle/<int:pk>', PostView.as_view(), name="detalle_post"),
    path('detalle_post/borrar/<int:pk>', PostDeleteView.as_view(), name='borrar_post')
    

] 


