from django.db.models.base import Model
from django.forms import ModelForm, DateInput
from menu.models import Ingrediente, Receta, Persona
from django import forms

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        