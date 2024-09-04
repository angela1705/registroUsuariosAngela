from django.db import models

# Create your models here.

class persona(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    email=models.EmailField(max_length=100,unique=True)
    fecha=models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre
    
    