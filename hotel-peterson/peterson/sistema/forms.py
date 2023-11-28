from django import forms

class buscarHab(forms.Form):
    personas = forms.IntegerField(widget=forms.NumberInput(attrs={'step': 1, 'max': 4, 'min': 0}))
    
