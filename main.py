from fastapi import FastAPI, HTTPException
import psycopg2
import psycopg2.extras
from databases.connection import conn #traigo la variable de conexion a postgres
from models.champions import Champ, Skill#datos de models
from controllers import control_champs, control_skill

app = FastAPI()

@app.get('/')
def root():
    return {"message":"hello world"}

#se crea la sigt estructura para llamar el contenido de control
app.include_router(control_champs.router, prefix="/api", tags=["Champions"])

app.include_router(control_skill.router, prefix="/api", tags=["Skills"])


        

        
@app.delete('/skill/{id}')
async def delete_skill(id:int):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """DELETE FROM "SKILLS" WHERE "SKILL_ID" = %s;"""
    values = (id) 
    try:
        cursor.execute(query, values)
        conn.commit()#hace que la info sea persistente en la bd
        return {"message":"usuario eliminado correctamente"}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a eliminar del champion:{e}")
    finally:
        cursor.close()
        conn.close()
