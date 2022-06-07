from django.contrib import admin
from aplicacion.models import Bicicleta, Duenio, Marca, Modelo, Tecnico
# Register your models here.
admin.site.register(Bicicleta)
admin.site.register(Duenio)
admin.site.register(Tecnico)
admin.site.register(Marca)
admin.site.register(Modelo)
