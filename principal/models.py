from django.db import models

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=60)
    telefono = models.CharField(max_length=30)
    asunto = models.TextField(max_length=2000)