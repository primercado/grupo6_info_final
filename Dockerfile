# Usar una imagen base de Python
FROM python:3.8-slim

# Crear un directorio para la aplicación
WORKDIR /app

# Copiar los archivos de la aplicación al directorio
COPY . /app

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Especificar el comando para iniciar la aplicación
CMD ["python", "app.py"]

