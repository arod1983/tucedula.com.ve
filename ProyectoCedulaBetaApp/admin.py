from django.contrib import admin
from ProyectoCedulaBetaApp.models import Cedula
 
# Register your models here.

class CedulaAdmin(admin.ModelAdmin):
    list_display=("nombre","cedula","estado","municipio","parroquia","direccion") #Panel Vista Lista    nombre=models.CharField(max_length=50)
    search_fields=("nombre","cedula","estado","municipio","parroquia","direccion") #Panel de Busqueda 
    list_filter=("nombre","cedula","estado","municipio","parroquia","direccion") # Panel Filtro de Busqueda
    
admin.site.register(Cedula,CedulaAdmin)
