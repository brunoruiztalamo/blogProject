from .models import Post
from django.views.generic import DetailView, ListView, CreateView
# Create your views here.

#Vista general de posts
class PostMain(ListView):
    model = Post
    template_name = 'postmain.html'



#Vista para agregar post
class AddPostView(CreateView):
    model = Post
    template_name = 'formulario_post.html'
    fields = '__all__'



#Vista para ver un post en particular
class PostView(DetailView):
    model = Post
    template_name = 'detalle_post.html'