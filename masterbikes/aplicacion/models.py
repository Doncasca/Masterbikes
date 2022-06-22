from datetime import date
from django.db import models

# Create your models here.

class Duenio(models.Model):
    duenio=models.CharField("Dueño",max_length=50)

    def __str__(self):
        return self.duenio

class Tecnico(models.Model):
    tecnico=models.CharField("Tecnico a cargo",max_length=50)

    def __str__(self):
        return self.tecnico

class Marca(models.Model):
    marca=models.CharField("Marca",max_length=50)

    def __str__(self):
        return self.marca

class Modelo(models.Model):
    modelo=models.CharField("Modelo",max_length=50,null=True)

    def __str__(self):
        return self.modelo

class Bicicleta(models.Model):
    code=models.AutoField(primary_key=True)
    duenio=models.ForeignKey(Duenio, on_delete=models.PROTECT)
    tecnico=models.ForeignKey(Tecnico, on_delete=models.PROTECT)
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo=models.ForeignKey(Modelo, on_delete=models.PROTECT)
    tiempo=models.IntegerField("Dias de mantenimiento",null=False)
    llegada=models.DateField("Dia de llegada (dd/mm/yyyy)",default=date.today)
    entrega=models.DateField(null=True,blank=True)


    def __str___(self):
        return str(self.code)


