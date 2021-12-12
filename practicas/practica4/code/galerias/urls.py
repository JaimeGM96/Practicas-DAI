from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('test_template', views.test_template, name='test_template'),
  path('lista_galerias',views.lista_galerias, name='lista_galerias'),
  path('<id>/detalle_galeria', views.detalle_galeria, name= 'detalle_galeria'),
  path('lista_cuadros',views.lista_cuadros, name='lista_cuadros'),
  path('<id>/detalle_cuadro', views.detalle_cuadro, name= 'detalle_cuadro'),
  path('nueva_galeria', views.nueva_galeria, name='nueva_galeria'),
  path('nuevo_cuadro', views.nuevo_cuadro, name='nuevo_cuadro'),
  path('<id>/modificar_galeria', views.modificar_galeria, name='modificar_galeria'),
  path('modificar_cuadro', views.modificar_cuadro, name='modificar_cuadro'),
  path('borrar_galeria', views.borrar_galeria, name='borrar_galeria'),
  path('borrar_cuadro', views.borrar_cuadro, name='borrar_cuadro'),
]