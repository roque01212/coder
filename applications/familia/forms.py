from django import forms

from .models import Familia, Zapas

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
            ),
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Ingresa tu nombre en MAYUSCULAS'
                }
            )
        }
       

class ZapasForm(forms.ModelForm):
    """Form definition for Famila."""

    class Meta:
        """Meta definition for Familaform."""

        model = Zapas
        fields = ('__all__')
        widgets={
            'fecha_v':forms.DateInput(
                attrs={
                    'type':'date',
                }
            
            )
       
        }

