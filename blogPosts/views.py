from django.shortcuts import render
from .models import Post
from .forms import formularioEdicion, formularioPost
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blogProfiles.models import Profile

# Create your views here.



#Vista general de posts
class PostMain(ListView):
    model = Post
    template_name = 'postmain.html'
    ordering = ['-timestamp']
    context_object_name = 'posts'

    def get_queryset(self):
        # Filtrar los posts por orden de timestamp
        return Post.objects.all().order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el perfil del usuario actual
        user_profile = Profile.objects.get(user=self.request.user)
        
        # Obtener todos los perfiles
        all_profiles = Profile.objects.all()
        
        context['user_profile'] = user_profile
        context['all_profiles'] = all_profiles
        context['profile_data'] = {
            'first_name': user_profile.user.first_name,
            'last_name': user_profile.user.last_name,
            # Agregar más campos si es necesario
        }
        
        return context



#Vista para agregar post
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = formularioPost
    template_name = 'formulario_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        return context


#Vista para ver mis post
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'detalle_posts.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        # Filtrar los posts del usuario autenticado
        return Post.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el perfil del usuario autenticado
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        
        return context



# Vista para borrar post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'borrar_post.html'
    success_url = reverse_lazy('postmain')
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context

# Vista para editar post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = formularioEdicion
    template_name = 'editar_post.html'
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context
    
    
    
class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detalle_post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener el perfil del usuario actual
        user_profile = Profile.objects.get(user=self.request.user)
        
        # Obtener el post específico usando el objeto self.object (provisto por DetailView)
        post = self.object
        
        context['user_profile'] = user_profile
        context['post_image_url'] = post.image.url
        context['user_avatar_url'] = user_profile.avatar.url
        
        # Agregar datos del perfil para mostrar en el template
        context['profile_data'] = {
            'first_name': user_profile.user.first_name,
            'last_name': user_profile.user.last_name,
            # Agregar más campos si es necesario
        }
        
        return context
    
    
 #Vista para ver mis posts   
class UserPostsListView(LoginRequiredMixin, ListView):
    template_name = 'posts_list.html'
    context_object_name = 'posts_list'
    #paginate_by = 10  # Opcional: para paginación si hay muchos 

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        return context