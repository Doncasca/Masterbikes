from audioop import maxpp
from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField(null=False)


    def __str__(self):
        return self.rut+ " - "+ self.nombre


class Bicicleta(models.Model):
    code=models.CharField(primary_key=True,max_length=10)
    duenio=models.CharField(max_length=50)
    tecnico=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50,null=True)
    tiempo=models.IntegerField(null=False)
    llegada=models.DateField(null=False)
    entrega=models.DateField(null=True)


    def __str___(self):
        return self.code+" - "+ self.duenio