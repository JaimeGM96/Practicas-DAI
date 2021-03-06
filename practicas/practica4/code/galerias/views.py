from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .models import Galeria, Cuadro
from .forms import GaleriaForm, CuadroForm

def index(request):
    return render(request, 'index.html')

def lista_galerias(request):
    context = {}

    context["dataset"] = Galeria.objects.all()

    return render(request, "lista_galerias.html", context)

def lista_cuadros(request):
    context = {}

    context["dataset"] = Cuadro.objects.all()

    return render(request, "lista_cuadros.html", context)

def nueva_galeria(request):
    if request.method == 'POST':
        form = GaleriaForm(request.POST)

        if form.is_valid():
            galeria = form.save()
            return HttpResponseRedirect('/')
    else:
        form = GaleriaForm()

    context = {
        'form': form
    }

    return render(request, 'galeria.html', context)

def nuevo_cuadro(request):
    if request.method == 'POST':
        form = CuadroForm(request.POST)

        if form.is_valid():
            cuadro = form.save()
            return HttpResponseRedirect('/')
    else:
        form = CuadroForm()

    context = {
        'form': form
    }

    return render(request, 'cuadro.html', context)

def modificar_galeria(request, id):
    galeria = Galeria.objects.get(id=id)
    form = GaleriaForm(initial={'nombre': galeria.nombre, 'dirección': galeria.dirección})
    
    if request.method == 'POST':
        form = GaleriaForm(request.POST, instance=galeria)
        if form.is_valid():
            form.save()
            model = form.instance
            return redirect('/lista_galerias')
    
    context = {
        'form': form
    }

    return render(request, 'modificar_galeria.html', context)

def modificar_cuadro(request, id):
    cuadro = Cuadro.objects.get(id=id)
    form = CuadroForm(initial={'nombre': cuadro.nombre, 'galeria': cuadro.galeria, 'autor': cuadro.autor})
    
    if request.method == 'POST':
        form = CuadroForm(request.POST, instance=cuadro)
        if form.is_valid():
            form.save()
            model = form.instance
            return redirect('/lista_cuadros')
    
    context = {
        'form': form
    }

    return render(request, 'modificar_cuadro.html', context)

def borrar_galeria(request, id):
    galeria = Galeria.objects.get(id=id)

    galeria.delete()

    return redirect('lista_galerias')

def borrar_cuadro(request, id):
    cuadro = Cuadro.objects.get(id=id)

    cuadro.delete()

    return redirect('lista_cuadros')
