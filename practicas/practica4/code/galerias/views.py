from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {
        'saludo': 'Juan'
    }   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)
