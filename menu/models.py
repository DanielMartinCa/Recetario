from django.db import models
from django.conf import settings
from django.db.models.aggregates import Avg

# Create your models here.


class Ingrediente(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    origen = models.CharField('Origen',max_length=100)#podrán ser animal, vegetal o derivado
    valor = models.IntegerField('ValorNutricional', null=True)# 1,2 ó 3 por simplificar y utilizar luego medias

    def __str__(self):
        return f'{self.nombre} {self.origen} {self.valor}'    
    class Meta:
        verbose_name = 'Ingrediente'

class Receta(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, verbose_name='Ingrediente')
    calidad = models.Avg( Ingrediente.valor)
    def __str__(self):
        return f'{self.nombre} {self.ingredientes} {self.calidad}'
    class Meta:
        verbose_name = 'Receta'

        