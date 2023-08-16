from flask import Flask, render_template, request
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
    return 'Bienvenido, a la API Clima'


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


@app.route('/consultar_clima', methods=['GET'])
def consultar_clima():
    return render_template('consultar_clima.html')

@app.route('/mostrar_clima', methods=['POST'])
def mostrar_clima():
    ciudad = request.form['ciudad']
    clima_actual = control.obtener_clima_actual(ciudad)
    return render_template('mostrar_clima.html', clima=clima_actual, ciudad=ciudad)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

