#./app/app.py
from flask import Flask, render_template, url_for
app = Flask(__name__)
          
# Funciones
def ordena_seleccion(m):
    for i in range(len(m)):
        min = i


        for j in range(i, len(m)):
            if m[j] < m[min]:
                min = j

        if min != i:
            m[i], m[min] = m[min], m[i]

def criba_eratostenes(x):
    numeros = list(range(2, x+1))
    i = 0

    while numeros[i]**2 <= x:
        for n in numeros:
            if n != numeros[i]:
              if n % numeros[i] == 0:
                numeros.remove(n)
        
        i += 1
    return numeros

def fibonacci(n):
    n0 = 0
    n1 = n2 = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        i = 3
        while i != n+1:
            n2 = n0 + n1
            n0, n1 = n1, n2
            i += 1

        return n2

# Páginas
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/ordena/<cadena>')
def ordena(cadena):
  return f'La cadena {cadena} ordenada sería: {ordena_seleccion(cadena)}'

@app.route('/eratostenes/<int:numero>')
def eratostenes(numero):
  return f'Resultado de la criba de eratostenes de {numero}: {criba_eratostenes(numero)}'

@app.route('/fibonacci/<int:numero>')
def fib(numero):
  return f'Resultado de la sucesión de Fibonacci para n = {numero}: {fibonacci(numero)}'

@app.route('/imagenes')
def mostrar_imagenes():
  return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page not found</title>
    </head>
    <body>
        <div>
          <h1 style="text-align:center;">Imagenes</h1>
          <img src="{{url_for('static', filename='imagen1.jpg')}}"/>
          <br/>
          <img src="{{url_for('static', filename='imagen2.jpg')}}"/>
          <br/>
          <img src="{{url_for('static', filename='imagen3.jpg')}}"/>
          <br/>
          <img src="{{url_for('static', filename='imagen4.jpg')}}"/>
        </div>
    </body>
    </html>
  '''

@app.errorhandler(404)
def page_not_found(error):
  return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page not found</title>
    </head>
    <body>
        <div style="position: absolute; top: 50%; left: 50%; margin-top: -50px; margin-left: -50px; width: 100px; height: 100px;">
          <h1 style="text-align:center;">404</h1>
          <p style="text-align:center;">Page not found</p>
        </div>
    </body>
    </html>
  '''