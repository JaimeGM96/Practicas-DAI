#./app/app.py
from flask import Flask, render_template, request, url_for, session, redirect, flash
import random, re

app = Flask(__name__)
app.secret_key = 'clave-secreta-para-el-uso-de-sesiones'
          
# Páginas
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error=None
  if request.method == 'POST':
    usuario = request.form['username']
    if usuario != 'admin' or \
            request.form['password'] != 'admin':
        error = 'Invalid credentials'
    else:
        flash('You were successfully logged in')
        session['username'] = usuario
        return redirect(url_for('index'))
  return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')