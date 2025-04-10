import psycopg2.extras
from contextlib import contextmanager #lib para crear funcion que abre y cierra recursos
from databases.connection import test_connection

@contextmanager
def get_cursor():
    """
    Context manager para obtener un cursor conectado a PostgreSQL.
    Al salir del bloque `with`, el cursor y la conexión se cierran automáticamente.
    """
    conn = test_connection()  # Conexión obtenida desde connection.py
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)  # Retorna resultados como diccionarios
    try:
        yield cursor
        conn.commit()  # Guarda cambios si todo fue exitoso (por si hay escritura)
    except Exception as e:
        conn.rollback()  # Revierte cambios si hay errores
        raise e
    finally:
        cursor.close()
        conn.close()

def execute_query(query: str, params: tuple = None):
    """
    Ejecuta una consulta SQL (solo lectura) y devuelve los resultados.
    - query: solo recibe consultas como string
    - params: tupla opcional de parámetros para queries con placeholders
    """
    with get_cursor() as cursor:
        cursor.execute(query, params or ())
        return cursor.fetchall()
