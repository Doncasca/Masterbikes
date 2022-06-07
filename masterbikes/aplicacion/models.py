from django.db import models
from datetime import date

# Create your models here.
class Bicicleta(models.Model):
    code=models.AutoField(primary_key=True)
    duenio=models.CharField("Dueño",max_length=50)
    tecnico=models.CharField("Tecnico a cargo",max_length=50)
    marca=models.CharField("Marca",max_length=50)
    modelo=models.CharField("Modelo",max_length=50,null=True)
    tiempo=models.IntegerField("Dias de mantenimiento",null=False)
    llegada=models.DateField(default=None)
    entrega=models.DateField(default=None,null=True)


    def __str___(self):
        return self.code+" - "+ self.duenio