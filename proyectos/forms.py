from django import forms
from .models import Entregable

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = '__all__'
