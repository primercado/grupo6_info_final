from flask import jsonify
from sqlalchemy import text
from database import db

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