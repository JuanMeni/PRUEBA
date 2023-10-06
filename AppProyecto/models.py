from django.db import models

# Create your models here.
class Cliente (models.Model):
    usuario = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.usuario} - {self.email}'
    
class Producto (models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
       return f'{self.nombre} - ${self.precio}'
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
       return f'{self.nombre}'