from django.db import models
from django.conf import settings
# Create your models here.


class Ingrediente(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    origen = models.CharField('Origen',max_length=100)
    

    def __str__(self):
        return f'{self.nombre} {self.origen}'
    
    class Meta:
        verbose_name = 'Ingrediente'
        