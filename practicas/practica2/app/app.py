#./app/app.py
from flask import Flask, render_template, url_for, request
import random, re
app = Flask(__name__)
          
# Páginas
@app.route('/')
def hello_world():
  return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')