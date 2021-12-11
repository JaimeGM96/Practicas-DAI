from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('test_template', views.test_template, name='test_template'),
  path('nueva_galeria', views.nueva_galeria, name='nueva_galeria'),
  path('nuevo_cuadro', views.nuevo_cuadro, name='nuevo_cuadro'),
]