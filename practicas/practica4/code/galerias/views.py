from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Galeria, Cuadro
from .forms import GaleriaForm, CuadroForm

def index(request):
    return render(request, 'index.html')

def test_template(request):
    if request.method == 'POST' and 'modificado' in request.POST:
        form = CuadroForm(request.POST)

        if form.is_valid():
            nombre = request.POST.get('nombre')
            galeria = request.POST.get('galeria')
            autor = request.POST.get('autor')
            Cuadro.objects.filter(nombre=nombre).update(nombre=nombre, galeria=galeria, autor=autor)
            return HttpResponseRedirect('/')
    else:
        form = CuadroForm()

    context = {
        'form': form
    }

    return render(request, 'test.html', context)

def lista_galerias(request):
    context = {}

    context["dataset"] = Galeria.objects.all()

    return render(request, "lista_galerias.html", context)

def lista_cuadros(request):
    context = {}

    context["dataset"] = Cuadro.objects.all()

    return render(request, "lista_cuadros.html", context)

def detalle_galeria(request, id):
    context = {}

    context["data"] = Galeria.objects.get(id=id)

    return render(request, "detalle_galeria.html", context)

def detalle_cuadro(request, id):
    context = {}

    context["data"] = Cuadro.objects.get(id=id)

    return render(request, "detalle_cuadro.html", context)

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
