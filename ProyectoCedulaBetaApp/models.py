from django.db import models

# Create your models here.

class Cedula(models.Model):
    nombre=models.CharField(max_length=50)
    cedula=models.IntegerField()
    estado=models.CharField(max_length=50)
    municipio=models.CharField(max_length=50)
    parroquia=models.CharField(max_length=50)
    direccion=models.TextField()
