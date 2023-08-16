# Trabajo Práctico Final Análisis de Datos

## Integrantes Grupo 6 :

- Mercado, Isaac Pablo Rubén
- Melisa Marlen Benitez
- Juan Jose Juarez
- Ariel Solis
- Andrea Mellinger
- Juan Carlos Olmedo
- Melani Rodríguez
- Mauro Federico Rascón
- Miguel Adrian Holzer Egea
- Gastón Darío Pérez Parra

## Descripción

La aplicación "API Clima" se encarga de proporcionar información climática de diferentes ciudades utilizando la API de OpenWeather. Esta información es almacenada en una base de datos PostgreSQL y es presentada a los usuarios a través de una API construida con Flask.
Componentes

1.  app.py:

Este es el archivo principal que aloja las rutas del servidor web y la configuración de la aplicación Flask.

```
Rutas:
    /: Mensaje de bienvenida.
    /clima/<string:ciudad>: Devuelve el clima de una ciudad específica.
    /ciudades: Obtiene todas las ciudades disponibles.
    /temperatura/<string:ciudad>: Obtiene la temperatura promedio de una ciudad.
    /clima: Renderiza una plantilla que muestra los datos del clima.
    /consultar_clima: Renderiza una plantilla para consultar el clima.
    /mostrar_clima: Renderiza el clima actual de una ciudad. 
```

2.  init.sql:

Script SQL para la creación de la tabla data_clima en la base de datos.

3.  conect_db.py:

Script de conexión a la base de datos y para insertar datos climáticos de un archivo CSV.

4.  extrac.py:

Obtiene datos del clima de la API de OpenWeather para diferentes ciudades y guarda estos datos en un archivo CSV.

5.  control.py:

Contiene funciones de ayuda para gestionar las peticiones a la base de datos y a la API de OpenWeather.

6.  data_base.py:

Inicialización de SQLAlchemy para la gestión de la base de datos.

7.  Dockerfile:

Especificaciones para crear la imagen Docker de la aplicación.

8.  docker-compose.yml:

Especificaciones para ejecutar la aplicación y la base de datos en contenedores Docker usando docker-compose.

9.  requeriments.txt:

Lista de dependencias Python necesarias para ejecutar la aplicación.

## Preparación:

- **Configuración del entorno:** Asegúrate de tener Docker, Docker Compose y python instalados en tu máquina.
    
- Abre una terminal o línea de comandos y ve al directorio raíz del proyecto.
    
- Crea un nuevo entorno virtual ejecutando el siguiente comando:
    
    `python -m venv venv`
    
- Activa el entorno virtual. En Windows, ejecuta:
    
    `venv\Scripts\activate`
    
- En macOS y Linux, ejecuta:
    
    `source venv/bin/activate`
    
- **Instalación de Dependencias:** Una vez que el entorno virtual esté activado, instala las dependencias del proyecto desde el archivo requirements.txt. Ejecuta el siguiente comando:
    

`pip install -r requirements.txt`

- **Variables de Entorno:** Configura las variables de entorno en un archivo .env. Este archivo debe contener:

```php-template
POSTGRES_DB=<nombre de la base de datos>
POSTGRES_USER=<nombre de usuario>
POSTGRES_PASSWORD=<contraseña>
SQLALCHEMY_DATABASE_URI=postgresql://<nombre de usuario>:<contraseña>@db:5432/<nombre de la base de datos>
```

- **Ejecución de extrac.py:** Antes de ejecutar la aplicación, debes correr el archivo extrac.py. Esto es necesario para extraer los datos climáticos y guardarlos en la base de datos.
- Dirigirse a la raíz del proyecto `app/` y ejecuta:
    
    `python extrac.py`
    

## Instrucciones de Despliegue

1.  **Construir y levantar los contenedores:** Dirígite al directorio app/ y ejecuta:

En Windows:

```
docker-compose up --build
docker-compose down
docker-compose up 
```

En Linux:

```
sudo docker-compose up --build
sudo docker compose down
sudo docker compose up 
```

2.  La aplicación estará disponible en http://localhost:5000/.


