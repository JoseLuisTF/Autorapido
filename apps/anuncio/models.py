from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from apps.usuario.models import Profile
# Create your models here.


class Vehiculo(models.Model):

    placa = models.CharField(max_length=8, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()
    color = models.CharField(max_length=10)
    kilometraje = models.IntegerField()
    cilindraje = models.IntegerField()
    nPuertas = models.IntegerField()
    aireAcondicionado = models.BooleanField()
    vidriosElectricos = models.BooleanField()
    tipoDireccion = models.CharField(max_length=20)
    tipoTransmision = models.CharField(max_length=20)
    airbag = models.BooleanField()
    nAsientos = models.BooleanField()
    alarma = models.BooleanField()
    sunroof = models.BooleanField()


class Anuncio(models.Model):
    usuario = get_user_model()
    titulo = models.TextField(max_length=30)
    precio = models.IntegerField()
    negociable = models.BooleanField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(max_length=300)
    ubicacionDepartamento = models.CharField(max_length=30)
    ubicacionCiudad = models.CharField(max_length=30)
    vendedor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    imagen = models.FileField(null=True, blank=True)
