from django.shortcuts import render
from .models import Post
from .forms import formularioEdicion, formularioPost
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blogProfiles.models import Profile
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.



# Vista general de posts
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
        user_profile = Profile.objects.get(user=self.request.user)
        all_profiles = Profile.objects.all()

        context['user_profile'] = user_profile
        context['all_profiles'] = all_profiles
        context['profile_data'] = {
            'first_name': user_profile.user.first_name,
            'last_name': user_profile.user.last_name,
            # Agregar más campos si es necesario
        }
        
        context['avatar_url'] = user_profile.avatar.url  # Agrega esta línea para el avatar

        return context



#Vista para agregar post
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = formularioPost
    template_name = 'formulario_post.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        response = super().form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse('detalle_post', args=[self.object.pk])
    
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


#Vista para el widget de buscar
class SearchView(TemplateView):
    template_name = 'buscar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        
        if query:
            profile_results = Profile.objects.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query) | Q(bio__icontains=query))
            post_results = Post.objects.filter(Q(title__icontains=query) | Q(header__icontains=query) | Q(content__icontains=query))
            context['search_results'] = {'profiles': profile_results, 'posts': post_results}
            context['query'] = query
        
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
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        return context
    
    
#Vista para ver detalle de un post    
class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detalle_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.get(user=self.request.user)
        post = self.object

        context['user_profile'] = user_profile
        context['user_avatar_url'] = user_profile.avatar.url  # Verifica esta línea

        if post.image:  # Verifica si el post tiene una imagen
            context['post_image_url'] = post.image.url
        else:
            context['post_image_url'] = None

        context['profile_data'] = {
            'first_name': user_profile.user.first_name,
            'last_name': user_profile.user.last_name,
            # Agregar más campos si es necesario
        }

        return context

    
    
 #Vista para ver todos los posts de un usuario   
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