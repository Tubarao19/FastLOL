from fastapi import FastAPI, HTTPException
import psycopg2
import psycopg2.extras
from core.databases.connection import conn #traigo la variable de conexion a postgres
from core.databases.models.champs.champions import Champ, Skill#datos de models

app = FastAPI()

@app.get('/')
def root():
    return {"message":"hello world"}

@app.get('/champs')
async def get_champs():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#regresar datos en Json
    query = 'SELECT * FROM "CHAMPIONS"'

    try:#intentar, para controlar los posibles fallos en consulta
        cursor.execute(query)#traer datos en especifico de la bd
        champs = cursor.fetchall()#almacenar los datos pedidos dentro de champs
        return champs #mostrar dichos datos almacenados
    except psycopg2.Error as err:#error al ejecutar el intento
        raise HTTPException(status_code=500, detail=f"error al conectar con postgres: {err}")
    finally:#se ejecuta independiente de si funciono o no el try
        cursor.close()#como buena practica se cierra el cursor o consulta

@app.post('/champ')
async def create_champ(champ:Champ):# se crea una variable que almacene lo de pydantic
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """INSERT INTO "CHAMPIONS" ("CHAMPS_NAME", "CHAMPS_HEALTH", "CHAMPS_AD", "CHAMPS_AP", "CHAMPS_MP", "CHAMPS_MANA") 
            VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (champ.CHAMPS_NAME, champ.CHAMPS_HEALTH, champ.CHAMPS_AD, champ.CHAMPS_AP, champ.CHAMPS_MP, champ.CHAMPS_MANA)

    #se crea values con el fin de no rellenar info de mas en el try y pasarle solo una variable
    try:
        cursor.execute(query, values)
        #champ_id = cursor.fetchone()["CHAMPS_ID"]
        conn.commit()#hace que la info sea persistente en la bd
        return {"message":"Champ agregado correctamente"}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    finally:
        cursor.close()