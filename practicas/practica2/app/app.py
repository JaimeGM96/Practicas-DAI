#./app/app.py
from flask import Flask
app = Flask(__name__)
          
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/ordena/<cadena>')
def ordena(cadena):
  return f'Hello, World!{cadena}'