from socket import fromshare
from django import forms

from .models import Familia

class FamiliaForm(forms.ModelForm):
    """Form definition for Famila."""

    class Meta:
        """Meta definition for Familaform."""

        model = Familia
        fields = ('__all__')
        # widgets={
        #     'parentezco':forms.CheckboxSelectMultiple(),
        #     'parentezco':forms.CheckboxSelectMultiple()
        # }
       

