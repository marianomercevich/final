from django.contrib import admin
from .models import *

class CascoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')
    search_fields = ('marca', 'tipo', 'talle', 'precio')
class CamperaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')
    search_fields = ('marca', 'tipo', 'talle', 'precio')
class GuanteAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'talle', 'precio')
    search_fields = ('marca', 'tipo', 'talle', 'precio')
class IndumentariaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'talle', 'precio')
    search_fields = ('tipo', 'marca', 'talle', 'precio')
class EquipajeAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'precio')
    search_fields = ('marca', 'tipo', 'precio')
class AccesorioAdmin (admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'precio')
    search_fields = ('marca', 'tipo', 'precio')
class RepuestoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'precio')
    search_fields = ('marca', 'tipo', 'precio')
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'tipo', 'precio')
    search_fields = ('marca', 'tipo', 'precio')
class EventoAdmin(admin.ModelAdmin):
    list_display = ('Titulo','Texto', 'Fecha', 'Estado', 'Valor_de_la_entrada', 'Pais', 'Provincia', 'Localidad', 'Direccion', 'Organizador','imagen')
    search_fields = ('Titulo','Texto', 'Fecha', 'Estado', 'Valor_de_la_entrada', 'Pais', 'Provincia', 'Localidad', 'Direccion', 'Organizador', 'imagen')

admin.site.register (casco, CascoAdmin)
admin.site.register (campera, CamperaAdmin)
admin.site.register (indumentaria, IndumentariaAdmin)
admin.site.register (equipaje, EquipajeAdmin)
admin.site.register (accesorio, AccesorioAdmin)
admin.site.register (repuesto, RepuestoAdmin)
admin.site.register (tecnologia, TecnologiaAdmin)
admin.site.register (evento, EventoAdmin)

admin.site.register(Avatar)

