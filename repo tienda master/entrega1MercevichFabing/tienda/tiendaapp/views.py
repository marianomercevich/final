from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required




def entrada (request):
    return redirect("index")

def index (request):
    return render (request, 'tiendaapp/index.html')


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request,"tiendaapp/index.html")
            else:
                return render(request,"tiendaapp/login.html")
        else:
            return render(request,"tiendaapp/login.html")
    
    form = AuthenticationForm()

    return render(request,"tiendaapp/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
       

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 

            form.save() 
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request,"tiendaapp/index.html")

            else:
                return render(request,"tiendaapp/register.html")


        return render(request,"tiendaapp/register.html",{"form":form})
    
    form = UserCreationForm()

    return render(request,"tiendaapp/register.html",{"form":form})


def logout_request(request):
    logout(request)
    return redirect("index")

@login_required
def editar_perfil(request):

    user = request.user 

    if request.method == "POST":
        
        form = UserEditForm(request.POST) 

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.nick_name = info["nick_name"]

            user.save()

            return render(request,"tiendaapp/index.html",{"form":form})
    
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})

    return render(request,"tiendaapp/editar_perfil.html", {"form":form})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return render(request,"tiendaapp/index.html")

    else:
        form = AvatarForm()
    
    return render(request,"tiendaapp/agregar_avatar.html",{"form":form})

def contacto(request):
    return render (request, 'tiendaapp/contacto.html')

def nosotros(request):
    return render (request, 'tiendaapp/nosotros.html')

def eventos(request):
    return render (request, 'tiendaapp/eventos.html')

# def crear_evento

# def editar_evento

# def eliminar_eveto    



@login_required
def tienda (request):
    return render (request, 'tiendaapp/tienda.html')

@login_required
def cascos (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cascos = casco.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()

            return render(request,"tiendaapp/cascos.html", {"cascos":cascos, "search":True, "busqueda":search})

    cascos = casco.objects.all()
    return render(request, 'tiendaapp/cascos.html', {"cascos":cascos, "search":False})
  
def crear_casco(request):

    
    if request.method == "POST":

        formulario = CascoFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            casco = casco(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            casco.save() 
            
            return redirect("cascos")

        return render(request,"tiendaapp/formulario_casco.html",{"form":formulario})
    

    formularioVacio = CascoFormulario()
    
    return render(request,"tiendaapp/formulario_casco.html",{"form":formulario})

def eliminar_casco(request, casco_id):

    # post
    Casco = casco.objects.get(id=casco_id)
    Casco.delete()

    return redirect("cascos")

def editar_casco(request, casco_id):

    Casco = casco.objects.get(id=casco_id)

    if request.method == "POST":

        formulario = CascoFormulario(request.POST)

        if formulario.is_valid():

            info_casco = formulario.cleaned_data
        
            Casco.marca = info_casco["marca"]
            Casco.tipo = info_casco["tipo"]
            Casco.talle = info_casco["talle"]
            Casco.precio = info_casco["precio"]
            Casco.save() # guardamos en la bd

            return redirect("cascos")
   
    formulario = CascoFormulario(initial={"marca":casco.marca,"tipo":casco.tipo, "talle":casco.talle, "precio":casco.precio })
    return render(request,"tiendaapp/formulario_casco.html",{"form":formulario})

@login_required
def camperas (request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            camperas = campera.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()

            return render(request,"tiendaapp/camperas.html", {"camperas":camperas, "search":True, "busqueda":search})

    camperas = campera.objects.all()
    return render(request, 'tiendaapp/camperas.html', {"camperas":camperas, "search":False})

def crear_campera (request):

    
    if request.method == "POST":

        formulario = CamperaFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Campera = campera(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            Campera.save() 
            
            return redirect("camperas")

        return render(request,"tiendaapp/formulario_campera.html",{"form":formulario})
    

    formulario = CamperaFormulario()

    return render(request,"tiendaapp/formulario_campera.html",{"form":formulario})

def eliminar_campera(request, campera_id):

    # post
    Campera = campera.objects.get(id=campera_id)
    Campera.delete()

    return redirect("camperas")

def editar_campera(request, campera_id):

    Campera = campera.objects.get(id=campera_id)

    if request.method == "POST":

        formulario = CamperaFormulario(request.POST)

        if formulario.is_valid():

            info_campera = formulario.cleaned_data
        
            Campera.marca = info_campera["marca"]
            Campera.tipo = info_campera["tipo"]
            Campera.talle = info_campera["talle"]
            Campera.precio = info_campera["precio"]
            Campera.save() # guardamos en la bd

            return redirect("camperas")
   
    formulario = CamperaFormulario(initial={"marca":campera.marca,"tipo":campera.tipo, "talle":campera.talle, "precio":campera.precio })
    return render(request,"tiendaapp/formulario_campera.html",{"form":formulario})

@login_required
def guantes (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            guantes = guante.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/guantes.html", {"guantes":guantes, "search":True, "busqueda":search})

    guantes = guante.objects.all()
    return render(request, 'tiendaapp/guantes.html', {"guantes":guantes, "search":False})
  
def crear_guante(request):

    
    if request.method == "POST":

        formulario = GuanteFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Guante = guante(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            Guante.save() # guardamos en la bd
            
            return redirect("guantes")
        return render(request,"tiendaapp/formulario_guante.html",{"form":formulario})
    
    formulario = GuanteFormulario()

    return render(request,"tiendaapp/formulario_guante.html",{"form":formulario})

def eliminar_guante(request, guante_id):

    # post
    Guante = guante.objects.get(id=guante_id)
    Guante.delete()

    return redirect("guantes")

def editar_guante(request, guante_id):

    Guante = guante.objects.get(id=guante_id)

    if request.method == "POST":

        formulario = GuanteFormulario(request.POST)

        if formulario.is_valid():

            info_guante = formulario.cleaned_data
        
            Guante.marca = info_guante["marca"]
            Guante.tipo = info_guante["tipo"]
            Guante.talle = info_guante["talle"]
            Guante.precio = info_guante["precio"]
            Guante.save() # guardamos en la bd

            return redirect("guantes")
   
    formulario = GuanteFormulario(initial={"marca":guante.marca,"tipo":guante.tipo, "talle":guante.talle, "precio":guante.precio })
    return render(request,"tiendaapp/formulario_guante.html",{"form":formulario})


def base(request):
    return render(request,"tiendaapp/base.html",{})

