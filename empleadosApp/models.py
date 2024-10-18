from django.db import models

# Create your models here.

class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):  #Es para ver el nombre del estado, y no un object
        return self.nombre


class Persona(models.Model):
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)
    telefono    = models.CharField(max_length=9)
    email       = models.EmailField()
    #Agregar un estado x FK
    estado      = models.ForeignKey(Estado,on_delete=models.CASCADE)
