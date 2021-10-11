#./app/app.py
from flask import Flask, render_template, url_for, request
import random, re
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

def generar_cadena(n):
    cadena = ''

    for i in range(n):
        aleatorio = random.randint(0, 1)
        if aleatorio == 0:
            cadena = cadena + "["
        else:
            cadena = cadena + "]"

    return cadena

def validar_expresiones(cadena):
    valida0 = re.search('.+\s+[A-Z]{1}', cadena)
    valida1 = re.search('.+@\w+\.\w+', cadena)
    valida2 = re.search('\d{4}-|\s+\d{4}-|\s+\d{4}-|\s+\d{4}', cadena)

    if valida0 or valida1 or valida2:
      return True
    else:
      return False

# Páginas
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/ordena/<cadena>')
def ordena(cadena):
  vector = list(map(int, cadena.split(",")))
  return f'La cadena {cadena} ordenada sería: {ordena_seleccion(vector)}'

@app.route('/eratostenes/<int:numero>')
def eratostenes(numero):
  return f'Resultado de la criba de eratostenes de {numero}: {criba_eratostenes(numero)}'

@app.route('/fibonacci/<int:numero>')
def fib(numero):
  return f'Resultado de la sucesión de Fibonacci para n = {numero}: {fibonacci(numero)}'

@app.route('/corchetes/<int:tam_cadena>')
def corchetes(tam_cadena):
  return f'Se ha generado la cadena {generar_cadena(tam_cadena)}'

@app.route('/expresiones_regulares/<expresion>')
def expresiones_regulares(expresion):
  if validar_expresiones(expresion):
    return f'La cadena {expresion} es valida'
  else:
    return f'La cadena {expresion} no es valida'

@app.route('/imagenes')
def mostrar_imagenes():
  return render_template('imagenes.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')