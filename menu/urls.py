from django.urls import  include, path
from menu.views import CreaIngrediente

urlpatterns= [
    path('crear_ingredientes/', CreaIngrediente.as_view(), name = 'crear_ingredientes'),
    ]