from django.urls import  include, path
from menu.views import CreaIngrediente, CreaReceta, subir_archivo, todos_ingredientes,todas_recetas,EliminarReceta, ModificarReceta, RecetasDetailView, SearchResultsListView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns= [
    path('crear_ingredientes/', CreaIngrediente.as_view(), name = 'crear_ingredientes'),
    path('subir_archivo/', subir_archivo, name = 'subir_archivo'),
    path('listaIngredientes/', todos_ingredientes, name = 'listaIngredientes'),
    path('crear_receta/', CreaReceta.as_view(), name ='crear_receta'),
    path('listaRecetas/', todas_recetas, name = 'listaRecetas'),
    path('detalle_receta/<int:pk>', RecetasDetailView.as_view(), name="detalle_receta"),
    path('buscarecetas/', SearchResultsListView.as_view(), name='buscarecetas' ),
    path('recetas/modificar/<int:pk>', ModificarReceta.as_view(), name='modificar_receta'),
    path('recetas/eliminar/<int:pk>', EliminarReceta.as_view(), name='eliminar_receta'),
    
    ]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()