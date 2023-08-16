import psycopg2
from time import sleep
from sqlalchemy import create_engine
import pandas as pd
import os

# Intenta conectarse a la base de datos en un bucle hasta que tenga éxito
while True:
    try:
        conn = psycopg2.connect(
            host="db",
            database=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD')
        )
        print ('Conexión Exitosa')
        break
    except psycopg2.OperationalError:
        print("Esperando por la database...")
        sleep(1)

# Crea un cursor para ejecutar comandos SQL
cur = conn.cursor()

# Nombre de la tabla y lectura del archivo CSV
nombre_tabla = "data_clima"

df = pd.read_csv('data_analytics/openweather/tiempodiario.csv')

# Creo un objeto de conexión de SQLAlchemy
engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))

# Convierte el DataFrame de Pandas en una tabla en la base de datos
df.to_sql(nombre_tabla, engine, if_exists="append", index=False)

# Cierra el cursor y la conexión
cur.close()

conn.close()