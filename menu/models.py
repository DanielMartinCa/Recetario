from django.db import models
from django.conf import settings
from django.urls import reverse



# Create your models here.

class Alergia(models.Model):
    nombre= models.CharField('Nombre de la alérgia', max_length=100)
        
    def __str__(self):
        return f'{self.nombre}'
    class Meta: 
        verbose_name= 'Alergia'

class Ingrediente(models.Model):
    tipos_origenes = (("An","Animal"),("Ve", "Vegetal"),("De", "Derivado"))
    nombre = models.CharField('Nombre',max_length=100)
    origen = models.CharField('Origen',max_length=100, choices=tipos_origenes)#podrán ser animal, vegetal o derivado
    alergeno = models.ForeignKey(Alergia, on_delete=models.SET_NULL,null=True,blank=True, verbose_name= 'Alergia')
    urlimage = models.CharField('Imagen', blank=True, max_length=1000)

    
    def __str__(self):
        return f'{self.nombre} {self.origen}'    
    class Meta:
        verbose_name = 'Ingrediente'


class Receta(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, verbose_name='Ingrediente')
    urlimage = models.CharField('Imagen', blank=True, max_length=1000)
    descripcion = models.TextField('Descripcion', blank=True)

    def __str__(self):
        return f'{self.nombre} {self.ingredientes}'
    class Meta:
        verbose_name = 'Receta'
    
    def muestra_ingredientes(self):
        '''Muestra género para admin'''
        return ', '.join([ing.nombre for ing in self.ingredientes.all()[:3]])
    muestra_ingredientes.short_description = 'Ingredientes'





    
        