from fastapi import HTTPException
import psycopg2
import psycopg2.extras
from databases.connection import conn
from models.champions import Champ, Skill


def get_champs():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#regresar datos en Json
    query = 'SELECT * FROM "CHAMPIONS";'

    try:#intentar, para controlar los posibles fallos en consulta
        cursor.execute(query)#traer datos en especifico de la bd
        champs = cursor.fetchall()#almacenar los datos pedidos dentro de champs
        return champs #mostrar dichos datos almacenados
    except psycopg2.Error as err:#error al ejecutar el intento
        raise HTTPException(status_code=500, detail=f"error al conectar con postgres: {err}")
    finally:#se ejecuta independiente de si funciono o no el try
        cursor.close()#como buena practica se cierra el cursor o consulta
        conn.close()