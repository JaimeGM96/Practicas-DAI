#./app/app.py
from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient
from flask_paginate import Pagination, get_page_args
from bson.json_util import dumps

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

# @app.route('/todos-pokemons')
# def todos_pokemons():
#   page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

#   pokemons = db.samples_pokemon.find()

#   lista_pokemons = []
#   for pokemon in pokemons:
#     app.logger.debug(pokemon)
#     lista_pokemons.append(pokemon)

#   pagination_pokemons = lista_pokemons[offset: offset + per_page]
#   pagination = Pagination(page=page, per_page=per_page, total=len(lista_pokemons), css_framework='bootstrap3')

#   return render_template('lista.html', pokemons=pagination_pokemons, page=page, per_page=per_page, pagination=pagination)

@app.route('/todos-pokemons')
def todos_pokemons():
  pokemons = db.samples_pokemon.find()

  lista_pokemons = []
  for pokemon in pokemons:
    app.logger.debug(pokemon)
    lista_pokemons.append(pokemon)
  
  return render_template('lista.html', lista_pokemons=lista_pokemons)

@app.route('/pokemons')
def get_pokemons():
  pokemons = db.samples_pokemon.find()
  response = dumps(pokemons)

  return response

@app.route('/pokemon/<int:id>')
def get_pokemon(id):
  pokemon = db.samples_pokemon.find_one({'id': id})
  respone = dumps(pokemon)

  return respone

@app.route('/aniade-pokemon/<string:pokemon_name>', methods=['POST'])
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
  response = jsonify('Pokemon insertado correctamente')
  response.status_code = 200
  return response

@app.route('/actualiza-pokemon/<id>', methods=['PUT'])
def update_pokemon_id(id):
  nuevo_nombre = "Pikachu"
  db.samples_pokemon.update_one({
    'id': id
  }, {
    "$set": {
      'name': nuevo_nombre
    }
  })
  response = jsonify('Pokemon modificado correctamente')
  response.status_code = 200
  return response

@app.route('/actualiza-pokemon/<string:nombre>', methods=['PUT'])
def update_pokemon_nombre(nombre):
  nuevo_nombre = "Pikachu"
  db.samples_pokemon.update_one({
    'name': nombre
  }, {
    "$set": {
      'name': nuevo_nombre
    }
  })
  response = jsonify('Pokemon modificado correctamente')
  response.status_code = 200
  return response

@app.route('/borrar-pokemon/<int:id>', methods=['DELETE'])
def delete_pokemon_id(id):
  db.samples_pokemon.delete_one({'id': id})
  response = jsonify('Pokemon eliminado correctamente')
  response.status_code = 200
  return response

@app.route('/borrar-pokemon/<string:nombre>', methods=['DELETE'])
def delete_pokemon_nombre(nombre):
  db.samples_pokemon.delete_one({'name': nombre})
  response = jsonify('Pokemon eliminado correctamente')
  response.status_code = 200
  return response

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')