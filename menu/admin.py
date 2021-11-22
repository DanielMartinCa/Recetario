from django.contrib import admin

# Register your models here.
from .models import Ingrediente, Receta

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display =['nombre','origen']
    
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display =['nombre','calidad']
   
