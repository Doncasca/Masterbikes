from django.db.models import fields
from django import forms
from aplicacion.models import Bicicleta

class frmBicicleta(forms.ModelForm):

    class Meta:
        model=Bicicleta
        fields='__all__'