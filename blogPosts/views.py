from .models import Post
from .forms import formularioEdicion, formularioPost
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



#Vista general de posts
class PostMain(ListView):
    model = Post
    template_name = 'postmain.html'
    ordering = ['-timestamp']



#Vista para agregar post
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = formularioPost
    template_name = 'formulario_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asignar el usuario actual al campo user
        return super().form_valid(form)



#Vista para ver mis post
class PostListView(ListView):
    model = Post
    template_name = 'detalle_posts.html'  # Nombre de tu plantilla HTML
    context_object_name = 'posts'
    
    def get_queryset(self):
        # Filtrar los posts por el usuario actual
        return Post.objects.filter(user=self.request.user)


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
    
    
class PostView(DetailView):
    model = Post
    template_name = 'detalle_post.html'
    context_object_name = 'post'