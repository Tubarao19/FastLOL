from core.config import conexion # Para acceder
import psycopg2

def test_connection():
    if not conexion.DATABASE_URL:
        raise ValueError("No se encontro la conexion a la bd registrada")
    return psycopg2.connect(conexion.DATABASE_URL)