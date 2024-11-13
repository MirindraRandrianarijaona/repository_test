from django import forms
from .models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['water', 'electricity', 'income']
        widgets = {
            'Eau': forms.NumberInput(attrs={'class': 'form-input'}),
            'Electricité': forms.NumberInput(attrs={'class': 'form-input'}),
            'Revenu': forms.NumberInput(attrs={'class': 'form-input'}),
        }