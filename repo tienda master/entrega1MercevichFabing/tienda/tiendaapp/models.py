from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

class casco(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    talle = models.CharField("Tipo", max_length=6)
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
