from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile



# Formulario Registro Usuario
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    username = forms.CharField(label="Nombre de usuario")  # Agregado el campo username
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    website = forms.URLField(label='Sitio web', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # Incluido 'username' en la lista de campos



#Datos extra de perfil de usuario
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']



#Datos indispensables de perfil de usuario
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.pk:  #Si esta instancia existe
            self.fields['username'].widget = forms.HiddenInput() #Entonces borra el mensaje  


    class Meta:
        model = UserProfile
        fields = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(self.user_form.fields)
        self.fields.update(self.user_profile_form.fields)
    
    def is_valid(self):
        return self.user_profile_form.is_valid() and self.user_form.is_valid()
    
    def save(self, commit=True):
        user = user_profile.user
        user_profile = self.instance
        if commit:
            user_profile.save()
            user_form_instance = self.user_form.save(commit=False)
            user_form_instance.pk = user.pk
            user_form_instance.save()
        return user_profile




