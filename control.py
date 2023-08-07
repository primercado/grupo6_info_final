from flask import jsonify
from sqlalchemy import text
from database import db
import requests

API_KEY = '1e2566e8d350e5d5a0c41ea6c5eacb8a'


def get_ciudad(ciudad):
    """Obtener datos del tiempo por nombre de ciudad"""
    query = text("SELECT * FROM data_clima WHERE ciudad = :ciudad")
    result = db.session.execute(query, {'ciudad': ciudad})
    rows = result.fetchall()
    if not rows:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    return jsonify([{
        'ciudad': row.ciudad,
        'fecha': str(row.fecha),
        'temperatura': row.temperatura,
        'humedad': row.humedad,
        'descripcion': row.descripcion,
    } for row in rows])


def get_todas_ciudades():
    """Obtener todas las ciudades disponibles"""
    query = text("SELECT DISTINCT ciudad FROM data_clima")
    result = db.session.execute(query)
    ciudades = [row[0] for row in result]
    if not ciudades:
        return jsonify({'mensaje': 'No se encontraron ciudades'}), 404

    return jsonify({'ciudades': ciudades})


def get_temp_prom_ciudad(city_name):
    """Obtener la temperatura promedio por nombre de ciudad"""
    query = text("SELECT AVG(temperatura) FROM data_clima WHERE ciudad = :city_name")
    result = db.session.execute(query, {'city_name': city_name}).fetchone()[0]
    if result is None:
        return jsonify({'mensaje': 'Ciudad no encontrada'}), 404

    return jsonify({'ciudad': city_name, 'temperatura_promedio': result})



def obtener_datos_clima():
    """Obtener todos los datos del clima"""
    query = text("SELECT ciudad, fecha, temperatura, humedad, descripcion FROM data_clima")
    result = db.session.execute(query)
    rows = result.fetchall()
    if not rows:
        return jsonify({'mensaje': 'No se encontraron datos del clima'}), 404

    data = [{
        'ciudad': row.ciudad,
        'fecha': str(row.fecha),
        'temperatura': row.temperatura,
        'humedad': row.humedad,
        'descripcion': row.descripcion,
    } for row in rows]

    return data



def obtener_coordenadas(nombre_ciudad, codigo_estado=None, codigo_pais=None, limite=5):
    url_base = "http://api.openweathermap.org/geo/1.0/direct?q="
    query = nombre_ciudad
    if codigo_estado:
        query += f",{codigo_estado}"
    if codigo_pais:
        query += f",{codigo_pais}"
    url = f"{url_base}{query}&limit={limite}&appid={API_KEY}"

    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        resultados = respuesta.json()
        if resultados:
            coordenadas = [(resultado['name'], resultado['lat'], resultado['lon']) for resultado in resultados]
            return coordenadas
        else:
            print(f"No se encontraron resultados para la ciudad {nombre_ciudad}.")
            return None
    else:
        print(f"Error en la llamada a la API: {respuesta.status_code}")
        return None
    


def obtener_clima_actual(nombre_ciudad, codigo_estado=None, codigo_pais=None, limite=5, exclude=None, units="metric", lang="es"):
    coordenadas = obtener_coordenadas(nombre_ciudad, codigo_estado, codigo_pais, limite)
    if coordenadas:
        latitud, longitud = coordenadas[0][1], coordenadas[0][2]
        url_clima = "https://api.openweathermap.org/data/3.0/onecall?"
        url = f"{url_clima}lat={latitud}&lon={longitud}&appid={API_KEY}"
        if exclude:
            url += f"&exclude={exclude}"
        url += f"&units={units}&lang={lang}"

        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos_clima = respuesta.json()
            return datos_clima
        else:
            print(f"Error en la llamada a la API: {respuesta.status_code}")
            return None
    else:
        print(f"No se encontraron coordenadas para la ciudad {nombre_ciudad}.")
        return None
    
