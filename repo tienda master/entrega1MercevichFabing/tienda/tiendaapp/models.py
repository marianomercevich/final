from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)
class casco(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    talle = models.CharField("Talle", max_length=6)
    precio = models.FloatField ("Precio $")
class campera(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    talle = models.CharField("Tipo", max_length=6)
    precio = models.FloatField ("Precio $")
class guante(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    talle = models.CharField("Tipo", max_length=6)
    precio = models.FloatField ("Precio $")
class indumentaria(models.Model):

    tipo = models.CharField("Tipo", max_length=30)
    marca = models.CharField("Marca", max_length=30)
    talle = models.CharField("Talle", max_length=30)
    precio = models.FloatField ("Precio $")
class equipaje(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    precio = models.FloatField ("Precio $")
class accesorio(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    precio = models.FloatField ("Precio $")
class repuesto(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    precio = models.FloatField ("Precio $")
class tecnologia(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    precio = models.FloatField ("Precio $")

class evento(models.Model):

    Titulo = models.CharField( "Titulo", max_length=50)
    Texto = models.CharField( "Texto", max_length=5000)
    Fecha = models.DateField("Fecha")
    Estado = models.CharField("Estado del evento", max_length=50)
    Valor_de_la_entrada = models.FloatField( "Valor de la entrada $")
    Pais = models.CharField("Pais ", max_length=50)
    Provincia = models.CharField(" Provincia ", max_length=50)
    Localidad = models.CharField(" Localidad ", max_length=50)
    Direccion = models.CharField(" Direccion ", max_length=50)
    Organizador = models.CharField(" Organizador ", max_length=50)
    imagen = models.ImageField(upload_to= 'static''imgen/', blank=True, null=True)
    
    # class comentario(models.Model):
    # post = models.ForeignKey('blog.Post', related_name='comentarios')
    # autor = models.CharField(max_length=200)
    # texto = models.TextField()
    # crear_dato = models.DateTimeField(default=timezone.now)
    # apro_comentario = models.BooleanField(default=False)

    # def approve(self):
    #     self.apro_comentario = True
    #     self.save()

    # def __str__(self):
    #     return self.text