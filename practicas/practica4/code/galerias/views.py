from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Galeria, Cuadro
from .forms import GaleriaForm, CuadroForm

def index(request):
    return render(request, 'index.html')

def test_template(request):
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

    return render(request, 'test.html', context)

def nueva_galeria(request):
    if request.method == 'POST':
        form = GaleriaForm(request.POST)

        if form.is_valid():
            galeria = form.save(commit=False)
            galeria.save()
            return HttpResponseRedirect('/')
    else:
        form = GaleriaForm()

    context = {
        'form': form
    }

    return render(request, 'test.html', context)