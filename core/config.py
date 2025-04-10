import os                       # Para acceder a las variables
from dotenv import load_dotenv  # Para cargar .env

load_dotenv()  # Carga las variables desde .env

class Conexion:
    DATABASE_URL = os.getenv("DATABASE_URL")

conexion = Conexion() #instancia que conecta con la base de datos