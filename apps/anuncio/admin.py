from django.contrib import admin

# Register your models here.

from apps.anuncio.models import Anuncio, Vehiculo

admin.site.register(Anuncio)
admin.site.register(Vehiculo)

