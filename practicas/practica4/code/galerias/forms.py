from .models import Galeria, Cuadro
from django.forms import ModelForm

class GaleriaForm(ModelForm):
  class Meta:
    model = Galeria
    fields = ['nombre', 'dirección']

class CuadroForm(ModelForm):
  class Meta:
    model = Cuadro
    fields = ['nombre', 'galeria', 'autor']