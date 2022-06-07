from django.contrib import admin
from aplicacion.models import Bicicleta
# Register your models here.
class admBicileta(admin.ModelAdmin):
    list_display=["code","duenio","tecnico","marca","modelo","tiempo","llegada","entrega"]
    list_editable=["duenio","tecnico","marca","modelo","tiempo","llegada","entrega"]
    list_filter=["duenio"]
    class Meta:
        model=Bicicleta

admin.site.register(Bicicleta,admBicileta)