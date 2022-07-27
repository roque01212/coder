
from django import forms

from .models import Familia

class FamiliaForm(forms.ModelForm):
    """Form definition for Famila."""

    class Meta:
        """Meta definition for Familaform."""

        model = Familia
        fields = ('__all__')
        widgets={
            'fecha_nac':forms.TextInput(
                attrs={
                    'placeholder':'27/07/2013'
                }
            )
        }
       

