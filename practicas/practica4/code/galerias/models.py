from django.db import models
from django.utils import timezone

class Galeria(models.Model):
  nombre     = Models.CharField(max_lenght=200)
  dirección  = Models.CharField(max_length=100)

  def __str__(self):
    return self.nombre

class Cuadro(models.Model):
  nombre           = Models.CharField(max_lenght=100)
  galeria          = Models.ForeingKey(Galeria, on_delete=models.CASCADE)
  autor            = Models.CharField(max_lenght=100)
  fecha_creación   = Models.DateField(default=timezone.now)