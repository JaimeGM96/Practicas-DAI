#./app/app.py
from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient

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

    return render_template('lista.html', elementos=lista_pokemons)

  return render_template('index.html')

@app.route('/mongo')
def mongo():
	pokemons = db.samples_pokemon.find()

	lista_pokemons = []
	for pokemon in pokemons:
		app.logger.debug(pokemon)
		lista_pokemons.append(pokemon)

	return render_template('lista.html', elementos=lista_pokemons)

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
  if request.method == 'POST':
    nombre = request.form['name']
    num = request.form['num']
    caramelo = nombre + ' Candy'
    tipos = request.form['types']
    lista_tipos = list(map(str, tipos.split(",")))
    pokemon = {
      'id': float(num), 
      'num': num, 
      'name': nombre, 
      'img': 'http://www.serebii.net/pokemongo/pokemon/001.png', 
      'type': lista_tipos, 
      'height': '0.71 m', 
      'weight': '6.9 kg', 
      'candy': caramelo, 
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
  else:
    pokemons = db.samples_pokemon.find({'name': 'Bulbasaur'})

    lista_pokemons = []
    for pokemon in pokemons:
      app.logger.debug(pokemon)
      lista_pokemons.append(pokemon)

    return str(lista_pokemons)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('error.html')