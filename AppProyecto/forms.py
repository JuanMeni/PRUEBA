from django import forms

class FormProducto(forms.Form):
    nombre=forms.CharField(max_length=40)
    descripcion=forms.CharField(max_length=80)
    precio=forms.DecimalField(max_digits=10, decimal_places=2)

class FormCategoria(forms.Form):
    nombre = forms.CharField(max_length=100)

class FormCliente (forms.Form):
    usuario=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    email=forms.EmailField()
    direccion=forms.CharField(max_length=40)