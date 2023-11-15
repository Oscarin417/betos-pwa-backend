from django import forms
<<<<<<< HEAD
from .models import Productos
=======
from .models import *
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'descripcion', 'imagen']
<<<<<<< HEAD
        widgets = {
=======
        widets = {
>>>>>>> b1eb03d7aa2737231177b545073b6893f970fb3a
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'})
        }