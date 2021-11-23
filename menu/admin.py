from django.contrib import admin

# Register your models here.
from .models import Ingrediente, Receta, Persona

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display =['nombre','origen']
    
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display =['nombre']
   
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display =['nombre', 'plato']