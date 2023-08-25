from django.urls import path
from .views import AddPostView, PostListView, PostView, PostMain, PostUpdateView, UserPostsListView, PostDeleteView, SearchView, AddCategoryView, CategoryView, LikeView



urlpatterns = [
    path('', PostMain.as_view(), name="postmain"),
    path('crearPost/', AddPostView.as_view(), name="formulario_post"),
    path('detalle_post/editar/<int:pk>', PostUpdateView.as_view(), name='editar_post'),
    path('detalle_posts/', PostListView.as_view(), name='detalle_posts'),
    path('detalle_post/detalle/<int:pk>', PostView.as_view(), name="detalle_post"),
    path('detalle_post/borrar/<int:pk>', PostDeleteView.as_view(), name='borrar_post'),
    path('posts_list/<int:user_pk>/', UserPostsListView.as_view(), name='posts_list'),
    path('buscar/', SearchView.as_view(), name='buscar'),
    path('agregar_categoria', AddCategoryView.as_view, name='agregar_categoria'),
    path('categoria/<str:cats>', CategoryView, name='categoria' ),
    path('like/<int:pk>', LikeView, name='like_post'),

] 


