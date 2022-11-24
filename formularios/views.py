from django.shortcuts import render
from django.views.generic import CreateView
from formularios.models import Contacto
from django.urls import reverse_lazy

class ContactoCrear(CreateView):
    model = Contacto
    success_url = reverse_lazy("home")
    fields = ['nombre', 'servicio', 'localidad', 'correo', 'numero_telefono', 'mensaje']
