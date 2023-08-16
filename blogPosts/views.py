from .models import Post
from .forms import formularioEdicion, formularioPost
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.



#Vista general de posts
class PostMain(ListView):
    model = Post
    template_name = 'postmain.html'
    ordering = ['-timestamp']



#Vista para agregar post
class AddPostView(CreateView):
    model = Post
    form_class = formularioPost
    template_name = 'formulario_post.html'
    #fields = '__all__'
    


#Vista para ver un post
class PostView(DetailView):
    model = Post
    template_name = 'detalle_post.html'



#Vista para editar post
class PostUpdateView(UpdateView):
    model = Post
    form_class = formularioEdicion
    template_name = 'editar_post.html'
    #fields = ['title', 'header', 'content', 'image']
    


#Vista para borrar post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'borrar_post.html'
    success_url = reverse_lazy('postmain')