from django.contrib import admin

# Register your models here.
from .models import Ingrediente, Receta, Alergia

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display =['nombre']
    
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display =['nombre']
   
@admin.register(Alergia)
class AlergiaAdmin(admin.ModelAdmin):
    list_display =['nombre']