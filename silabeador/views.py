from silabeador import app
from silabeador.tools import pilengua
from flask import jsonify
import requests




@app.route("/pilengua/<frase>")
def enlenguapi(frase):
    respuesta = pilengua(frase)
    d = {
        'original': frase, 
        'pilengua': respuesta
    }
    return jsonify(d)

@app.route("/pelicula/<palabra>") #Vamos a hacer la llamada a la Api utilizando la libreria requests de python
def pelicula(palabra):
    url = "http://www.omdbapi.com/?s={}&apikey=b8d84844"

    resultado = requests.get(url.format(palabra)) #Hago la peticion con requests y meto lo que devuelva en la variable resultado. El atributo .format(palabra) es el texto que escriba para la busqueda. Esta peticion es sincrona, hasta que no devuelva algo no va a pasar a la siguiente linea. 
    if resultado.status_code == 200: #Si todo ha ido bien en la peticion
        peliculas = resultado.json() #El resultado lo devuelve en un json y lo guarda en la variable peliculas
        if peliculas['Response'] == "False": #Asi se pregunta en Python sobre una clave del diccionario, en este caso Response, que es una clave del diccionario peliculas, entre corchetes y entre comillas
            return jsonify({'status':"Error", "msg": "No se han encontrado resultados"}) #En caso de que no se hayan encontrado resultados, devuelvo una respuesta propia mia en foma de diccionario
        
        return jsonify({"Peliculas": peliculas["Search"], 'status': "Success"}) #Si la busqueda tiene exito, guardo los resultados en la clave "Peliculas", que la sustituyo en este linea por la clave original que es "Search"