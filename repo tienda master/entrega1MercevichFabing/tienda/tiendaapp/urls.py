from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name = 'index'), 

    path('login', login_request, name = 'login'), 
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),

    path ('nosotros/', nosotros, name = 'nosotros'),  
    path ('contacto/', contacto, name = 'contacto'),  
    path ('eventos/', eventos, name = 'eventos'),

    path ('tienda/', tienda, name = 'tienda'),

    path('cascos/', cascos, name = 'cascos'),
    path('crear_casco/', crear_casco, name="crear_casco"),
    path('eliminar_casco/<casco_id>/', eliminar_casco, name="eliminar_casco"),
    path('editar_casco/<casco_id>/', editar_casco, name="editar_casco"),

    path('camperas/', camperas, name = 'camperas'),
    path('crear_campera/', crear_campera, name="crear_campera"),
    path('eliminar_campera/<campera_id>/', eliminar_campera, name="eliminar_campera"),
    path('editar_campera/<campera_id>/', editar_campera, name="editar_campera"),

    path('guantes/', guantes, name = 'guantes'),
    path('crear_guante/', crear_guante, name="crear_guante"),
    path('eliminar_guante/<guante_id>/', eliminar_guante, name="eliminar_guante"),
    path('editar_guante/<guante_id>/', editar_guante, name="editar_guante"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)