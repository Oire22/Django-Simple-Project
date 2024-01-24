from django.db import models

# Create your models here.
class Member(models.Model):
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    telefono = models.IntegerField(null = True)
    fecha_inscrip = models.DateField(null = True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
