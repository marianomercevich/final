from .models import Avatar
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CascoFormulario(forms.Form):

    marca = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    precio = forms.FloatField()

class CamperaFormulario(forms.Form):


    marca = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    precio = forms.FloatField ()

class GuanteFormulario(forms.Form):


    marca = forms.CharField()
    tipo = forms.CharField()
    talle = forms.CharField()
    precio = forms.FloatField()

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    nick_name = forms.CharField(label="Nick-Name")
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'nick_name']

        # help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']