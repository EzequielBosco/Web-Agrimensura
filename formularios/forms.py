from django.forms import ModelForm
from formularios.models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'servicio', 'localidad', 'correo', 'telefono', 'mensaje')