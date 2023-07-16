from django import forms

class CrearPoema(forms.Form):
    autor = forms.CharField(max_length=20)
    titulo = forms.CharField(max_length=20)
    fecha_publicacion = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'), input_formats=('%d/%m/%Y'))
    portada = forms.ImageField(required=False)
    
class BusquedaPoema(forms.Form):
    titulo = forms.CharField(max_length=20, required=False)