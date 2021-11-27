#./app/app.py
from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)
app.secret_key = 'clave-secreta-para-el-uso-de-sesiones'
client = MongoClient("mongo", 27017)
db = client.SampleCollections 
          
# Páginas
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    clave = request.form['clave']
    valor = request.form['valor']
    
    if clave == 'name':
      pokemons = db.samples_pokemon.find({'name': valor})
    else:
      pokemons = db.samples_pokemon.find({'num': valor})

    lista_pokemons = []
    for pokemon in pokemons:
      app.logger.debug(pokemon)
      lista_pokemons.append(pokemon)

    return render_template('info_pokemon.html', elementos=lista_pokemons)

  return render_template('index.html')

@app.route('/mongo')
def mongo():
  page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

  pokemons = db.samples_pokemon.find()

  lista_pokemons = []
  for pokemon in pokemons:
    app.logger.debug(pokemon)
    lista_pokemons.append(pokemon)

  pagination_pokemons = lista_pokemons[offset: offset + per_page]
  pagination = Pagination(page=page, per_page=per_page, total=len(lista_pokemons), css_framework='bootstrap3')

  return render_template('lista.html', pokemons=pagination_pokemons, page=page, per_page=per_page, pagination=pagination)

@app.route('/pokemons')
def get_pokemons():
  pokemons = db.samples_pokemon.find()

  lista_pokemons = []
  for pokemon in pokemons:
    app.logger.debug(pokemon)
    lista_pokemons.append(pokemon)

  return jsonify(str(lista_pokemons))

@app.route('/pokemons/<string:pokemon_name>')
def get_pokemon(pokemon_name):
  pokemons = db.samples_pokemon.find({'name': pokemon_name})

  lista_pokemons = []
  for pokemon in pokemons:
    app.logger.debug(pokemon)
    lista_pokemons.append(pokemon)

  return jsonify(str(lista_pokemons))

@app.route('/pokemons/<string:pokemon_name>', methods=['POST'])
def add_pokemon(pokemon_name):
  pokemon = {
    'id': 161.0, 
    'num': '161', 
    'name': pokemon_name,
    'type': ['Grass'], 
    'height': '0.71 m', 
    'weight': '6.9 kg', 
    'candy_count': 25.0, 
    'egg': '2 km', 
    'spawn_chance': 0.69, 
    'avg_spawns': 69.0, 
    'spawn_time': '20:00', 
    'multipliers': [1.58], 
    'weaknesses': [
      'Fire', 
      'Ice', 
      'Flying', 
      'Psychic'
    ]
  }

  db.samples_pokemon.insert_one(pokemon)
  return "Insertado correctamente"

@app.route('/pokemons/<string:pokemon_name>', methods=['PUT'])
def update_pokemon(pokemon_name):
  nuevo_nombre = "Nuevo nombre"
  db.samples_pokemon.update(
    {'name': nuevo_nombre}
  )
  return "Actualizado correctamente"

@app.route('/pokemons/<string:pokemon_name>', methods=['DELETE'])
def delete_pokemon(pokemon_name):
  db.samples_pokemon.delete(
    {'name': pokemon_name}
  )
  return "Eliminado correctamente"

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')