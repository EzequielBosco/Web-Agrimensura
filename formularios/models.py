from django.db import models

contacto_servicio = [
    (1, 'Mensura'),
    (2, 'Estado parcelario'),
    (3, 'Relevamiento'),
    (4, 'Amojonamiento'),
    (5, 'Replanteo'),
    (6, 'Subdivision en Propiedad horizontal'),
    (7, 'Unificación'),
    (8, 'Loteo'),
    (9, 'Plano de usucapión'),
    (10, 'Barrio cerrado o club de campo'),
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    servicio = models.IntegerField(null=False, blank=False, choices=contacto_servicio)
    localidad = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50)
    numero_telefono = models.CharField(max_length=20)
    mensaje = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Trabajo: {self.servicio} |  Fecha: {self.fecha}"
