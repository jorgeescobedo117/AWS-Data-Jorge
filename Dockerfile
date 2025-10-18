<<<<<<< HEAD
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
=======
# Imagen base con Python
FROM python:3.11

# Instalar dependencias necesarias
RUN pip install --no-cache-dir streamlit mysql-connector-python pandas matplotlib seaborn python-dotenv

# Crear directorio de trabajo
WORKDIR /app

# Copiar el código de la app
COPY app.py /app/

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando para correr Streamlit
>>>>>>> 506eb6f8276f6d15694c089f50db5a4df4e6a817
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
