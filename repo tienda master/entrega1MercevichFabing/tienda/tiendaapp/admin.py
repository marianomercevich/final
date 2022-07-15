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



admin.site.register (casco, CascoAdmin)
admin.site.register (campera, CamperaAdmin)
admin.site.register (guante, GuanteAdmin)

admin.site.register(Avatar)

