from fastapi import FastAPI, HTTPException
# from services.service_champs import 
from databases.connection import conn, cursor
import psycopg2

app = FastAPI()

# @app.get('/champs')
# async def get_champs():
#     try:

#     except psycopg2.Error as err:#error al ejecutar el intento
#         raise HTTPException(status_code=500, detail=f"error al conectar con postgres: {err}")
#     finally:#se ejecuta independiente de si funciono o no el try
#         cursor.close()#como buena practica se cierra el cursor o consulta
#         conn.close()