#./app/app.py
from flask import Flask, render_template, request, url_for, session, redirect, flash
import random, re

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
          
# Páginas
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error=None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
        error = 'Invalid credentials'
    else:
        flash('You were successfully logged in')
        return redirect(url_for('index'))
  return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')