from .models import Post, Category
from .forms import formularioEdicion, formularioPost
from blogProfiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
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
# En tu vista de creación de un nuevo post
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = formularioPost
    template_name = 'formulario_post.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        form.instance.Category_id = 'category_id'
        
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



# Vista para el widget de buscar
class SearchView(TemplateView):
    template_name = 'buscar.html'

    def get_queryset(self):
        return Profile.objects.all().order_by('user__id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        
        if query:
            profile_results = Profile.objects.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query) | Q(bio__icontains=query)).order_by('user__id')
            post_results = Post.objects.filter(Q(title__icontains=query) | Q(header__icontains=query) | Q(content__icontains=query)).order_by('-pk')
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

    def get_queryset(self):
        return Profile.objects.all().order_by('-user__id')

    def get_object(self, queryset=None):
        # Obtener el ID del post desde la URL
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = Profile.objects.get(user=self.request.user)
        post = self.object

        context['user_profile'] = user_profile
        context['user_avatar_url'] = user_profile.avatar.url

        if post.image:
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

    def get_context_data(self, request, **kwargs):
        user_profile = Profile.objects.get(user=request.user)
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        context['user_profile'] = user_profile
        context['user_avatar_url'] = user_profile.avatar.url
        return context



#Vista para agregar categoria
class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'agregar_categoria.html'
    fields = ['name']
    
    
    
#Vista para ver categorias (Es mas practico usar una funcion antes de una clase en este caso)
def CategoryView(request, cats):
    # Busca el objeto Category con el nombre 'cats', devuelve un 404 si no existe
    category = get_object_or_404(Category, name=cats)
    # Filtrar Post relacionados con categoria
    category_posts = Post.objects.filter(category=category)
    
    return render(request, 'categorias.html', {'cats': cats, 'category_posts': category_posts})


