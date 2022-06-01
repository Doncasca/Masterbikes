from django.contrib import admin
from aplicacion.models import Persona,Bicicleta
# Register your models here.
class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","mail"]
    list_editable=["nombre","apellido","mail"]
    list_filter=["nombre"]
    class Meta:
        model=Persona

admin.site.register(Persona,admPersona)

class admBicileta(admin.ModelAdmin):
    list_display=["code","duenio","tecnico","marca","modelo","tiempo","llegada","entrega"]
    list_editable=["duenio","tecnico","marca","modelo","tiempo","llegada","entrega"]
    list_filter=["duenio"]
    class Meta:
        model=Bicicleta

admin.site.register(Bicicleta,admBicileta)