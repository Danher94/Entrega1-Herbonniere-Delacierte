from django import forms

class BusquedaPoema(forms.Form):
    titulo = forms.CharField(max_length=20, required=False)