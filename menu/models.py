from django.db import models
from django.conf import settings



# Create your models here.


class Ingrediente(models.Model):
    nombre = models.CharField('Nombre',max_length=100)
    origen = models.CharField('Origen',max_length=100)#podrán ser animal, vegetal o derivado
    alergeno = models.CharField('alergeno', max_length=100, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.origen}'    
    class Meta:
        verbose_name = 'Ingrediente'

class Receta(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, verbose_name='Ingrediente')
    
    
    def __str__(self):
        return f'{self.nombre} {self.ingredientes}'
    class Meta:
        verbose_name = 'Receta'

class Persona(models.Model):
    nombre= models.CharField('Nombre del comensal', max_length=100)
    alergia = models.ManyToManyField(Ingrediente,verbose_name= 'Alergias del comensal')
    plato = models.ForeignKey('Receta',on_delete=models.SET_NULL, null=True, verbose_name='Plato favorito')
    
    
    def __str__(self):
        return f'{self.nombre} {self.plato}'

    class Meta: 
        verbose_name= 'Persona'

class Imagen(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='título')
    file = models.ImageField(upload_to="imagenes/%Y/%m/%d/", verbose_name='imagen',
        height_field= 'alto', width_field='ancho')
    
    ancho = models.IntegerField(editable=False, default=0)
    alto = models.IntegerField(editable=False, default=0)
    fecha_subida = models.DateTimeField(verbose_name='Fecha de subida', auto_now_add=True,
        db_index=True, blank=True, null=True)
    subida_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Subida por usuario',
        null=True, blank=True, editable=False, 
        on_delete=models.SET_NULL
    )
    

    def __str__(self):
        return self.titulo
    
        