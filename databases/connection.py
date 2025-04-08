from core.config import settings
import psycopg2

def get_connection():
    if not settings.DATABASE_URL:
        raise ValueError("No se encontro la conexion a la bd registrada")
    return psycopg2.connect(settings.DATABASE_URL)