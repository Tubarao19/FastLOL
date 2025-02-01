from fastapi import FastAPI, HTTPException
import psycopg2
from core.databases.connection import conn #traigo la variable de conexion a postgres
from core.databases.models.champs.champions import Champ, Skill#datos de models

app = FastAPI()

@app.get('/')
def root():
    return {"message":"hello world"}

@app.get('/champs')
async def get_champs():
    cursor = conn.cursor(dictionay=True)#regresar datos en Json
    query = "SELECT * FROM CHAMPIONS"

    try:#intentar, para controlar los posibles fallos en consulta
        cursor.execute(query)#traer datos en especifico de la bd
        champs = cursor.fetchall()#almacenar los datos pedidos dentro de champs
        return champs #mostrar dichos datos almacenados
    except psycopg2.Error as err:#error al ejecutar el intento
        raise HTTPException(status_code=500, detail=f"error al conectar con postgres: {err}")
    finally:#se ejecuta independiente de si funciono o no el try
        cursor.close()#como buena practica se cierra el cursor o consulta