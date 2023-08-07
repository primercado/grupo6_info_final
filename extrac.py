import requests
import os
import time

CIUDADES = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
COORDENADAS = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
API_KEY = '1e2566e8d350e5d5a0c41ea6c5eacb8a'
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall/timemachine'

# Función para obtener los datos del clima
def get_data(ciudad, coordenadas):
    for i in range(5):  # Para obtener datos de los últimos 5 días
        timestamp = int(time.time()) - i * 24 * 60 * 60  # Timestamp para el día actual menos i días
        url = f'{BASE_URL}?{coordenadas}&dt={timestamp}&appid={API_KEY}'
        response = requests.get(url)
    
        if response.status_code == 200:
            data = response.json()
            guarda_data_csv(data, ciudad)
        else:
            print(f'Error al obtener los datos del clima para {ciudad}. Código de estado: {response.status_code}')

# Función para guardar los datos en un CSV
def guarda_data_csv(data, ciudad):
    directorio = os.path.join("data_analytics", "openweather")
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    archivo = os.path.join(directorio, f"tiempodiario.csv")
    
    # Comprobar si el archivo ya existe para decidir si agregar el encabezado
    encabezado_necesario = not os.path.exists(archivo)

    with open(archivo, 'a') as file:
        if encabezado_necesario:
            file.write("ciudad,fecha,temperatura,humedad,descripcion\n")
        
        fecha = time.strftime('%Y-%m-%d', time.gmtime(data['data'][0]['dt']))
        temp = data['data'][0]['temp']
        humedad = data['data'][0]['humidity']
        descripcion= data['data'][0]['weather'][0]['description']
        
        file.write(f"{ciudad},{fecha},{temp},{humedad},{descripcion}\n")


if __name__ == "__main__":
    for ciudad, coordenada in zip(CIUDADES, COORDENADAS):
        get_data(ciudad, coordenada)