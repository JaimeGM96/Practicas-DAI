#./app/app.py
from flask import Flask, render_template, request, url_for, session, redirect, flash
import random, re
from pickleshare import *

app = Flask(__name__)
app.secret_key = 'clave-secreta-para-el-uso-de-sesiones'
db = PickleShareDB('db_pickleshare/')
          
# Páginas
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
  if request.method == 'POST':
    db['username'] = request.form['username']
    db['password'] = request.form['password']
    flash('Te has registrado correctamente')
    return redirect(url_for('index'))

  return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error=None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username != db['username'] or \
            password != db['password']:
        error = 'Invalid credentials'
    else:
        flash('Bienvenido ' + username)
        session['username'] = username
        return redirect(url_for('index'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/ordena', methods=['GET', 'POST'])
def ordena():
  resultado = None
  if request.method == 'POST':
    datos = request.form['datos']
    resultado = list(map(int, datos.split(",")))
    ordena_seleccion(resultado)

  return render_template('ejercicios.html', resultado=resultado)

@app.route('/eratostenes', methods=['GET', 'POST'])
def eratostenes():
  resultado = None
  if request.method == 'POST':
    datos = request.form['datos']
    resultado = criba_eratostenes(int(datos))

  return render_template('ejercicios.html', resultado=resultado)

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
  resultado = None
  if request.method == 'POST':
    datos = request.form['datos']
    resultado = fibonacci(int(datos))

  return render_template('ejercicios.html', resultado=resultado)

@app.route('/corchetes', methods=['GET', 'POST'])
def corchetes():
  resultado = None
  if request.method == 'POST':
    datos = request.form['datos']
    resultado = generar_cadena(int(datos))

  return render_template('ejercicios.html', resultado=resultado)

@app.route('/expresiones_regulares', methods=['GET', 'POST'])
def expresiones_regulares():
  resultado = None
  if request.method == 'POST':
    datos = request.form['datos']
    resultado = validar_expresiones(datos)
    if resultado:
      resultado = "cadena válida"
    else:
      resultado = "cadena no válida"

  return render_template('ejercicios.html', resultado=resultado)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')


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