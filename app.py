from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database import db
import control
import os

app = Flask (__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Inicializa la instancia de SQLAlchemy con la aplicación Flask
db.init_app(app)


@app.route('/')
def inicio():
    return 'Bienvenido, a la API Clima pinche gato'


@app.route('/clima/<string:ciudad>', methods=['GET'])
def ruta_clima(ciudad):
    return control.get_ciudad(ciudad)


@app.route('/ciudades', methods=['GET'])
def ruta_ciudades():
    return control.get_todas_ciudades()


@app.route('/temperatura/<string:ciudad>', methods=['GET'])
def ruta_temperatura(ciudad):
    return control.get_temp_prom_ciudad(ciudad)


@app.route('/clima')
def clima():
    data = control.obtener_datos_clima()
    return render_template('clima.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

