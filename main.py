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
        
@app.get('/skill')
async def get_skill():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#regresar datos en Json
    query = 'SELECT * FROM "SKILLS";'

    try:#intentar, para controlar los posibles fallos en consulta
        cursor.execute(query)#traer datos en especifico de la bd
        skills = cursor.fetchall()#almacenar los datos pedidos dentro de la variable
        return skills #mostrar dichos datos almacenados
    except psycopg2.Error as err:#error al ejecutar el intento
        raise HTTPException(status_code=500, detail=f"error al conectar con postgres: {err}")
    finally:#se ejecuta independiente de si funciono o no el try
        cursor.close()#como buena practica se cierra el cursor o consulta
        conn.close()

@app.post('/champ')
async def create_champ(champ:Champ):# se crea una variable que almacene lo de pydantic
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """INSERT INTO "CHAMPIONS" 
            ("CHAMPS_NAME", 
            "CHAMPS_HEALTH", 
            "CHAMPS_AD", 
            "CHAMPS_AP", 
            "CHAMPS_MP", 
            "CHAMPS_MANA") 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING "CHAMPS_ID", "CHAMPS_NAME";"""
            
    values = (champ.CHAMPS_NAME, 
            champ.CHAMPS_HEALTH, 
            champ.CHAMPS_AD, 
            champ.CHAMPS_AP, 
            champ.CHAMPS_MP, 
            champ.CHAMPS_MANA)

    #se crea values con el fin de no rellenar info de mas en el try y pasarle solo una variable
    try:
        cursor.execute(query, values)
        champ_data = cursor.fetchone()
        conn.commit()#hace que la info sea persistente en la bd
        return {"message":"Champ agregado correctamente", "CHAMPS_ID":champ_data, "CHAMPS_NAME":champ_data}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    finally:
        cursor.close()
        conn.close()

@app.post('/skill')
async def create_skill(skill:Skill):# se crea una variable que almacene lo de pydantic
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """INSERT INTO "SKILLS" 
            ("SKILL_NAME", 
            "SKILL_MANA_COST", 
            "CHAMPS_ID" 
            VALUES (%s, %s, %s) RETURNING "SKILL_ID", "SKILL_NAME";"""
            
    values = (skill.SKILL_NAME,
            skill.SKILL_MANA_COST,
            skill.CHAMPS_ID)

    #se crea values con el fin de no rellenar info de mas en el try y pasarle solo una variable
    try:
        cursor.execute(query, values)
        skill_data = cursor.fetchone()
        conn.commit()#hace que la info sea persistente en la bd
        return {"message":"nueva habilidad agregada correctamente", "SKILL_ID":skill_data, "SKILL_NAME":skill_data}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    finally:
        cursor.close()
        conn.close()
        
@app.put('/champ/{id}')
async def update_champ(champ:Champ, id:int):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """UPDATE "CHAMPIONS"
    SET "CHAMPS_NAME" = %s,
    "CHAMPS_HEALTH" = %s,
    "CHAMPS_AD" = %s,
    "CHAMPS_AP" = %s,
    "CHAMPS_MP" = %s,
    "CHAMPS_MANA" = %s
    WHERE "CHAMPS_ID" = %s;"""
    
    values = (champ.CHAMPS_NAME,
            champ.CHAMPS_HEALTH,
            champ.CHAMPS_AD,
            champ.CHAMPS_AP,
            champ.CHAMPS_MP,
            champ.CHAMPS_MANA,
            id)
    
    try:
        cursor.execute(query, values)
        conn.commit()#hace que la info sea persistente en la bd
        return {"message":"Champ actualizado correctamente"}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    finally:
        cursor.close()
        conn.close()
        
@app.put('/skill/{id}')
async def update_skill(skill:Skill, id:int):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """UPDATE "SKILLS"
    SET "SKILL_NAME" = %s,
    "SKILL_MANA_COST" = %s,
    "CHAMPS_ID" = %s
    WHERE "SKILL_ID" = %s;"""
    
    values = (skill.SKILL_NAME,
            skill.SKILL_MANA_COST,
            skill.CHAMPS_ID,
            id)
    
    try:
        cursor.execute(query, values)
        conn.commit()#hace que la info sea persistente en la bd
        return {"message":"habilidad actualizada correctamente"}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    finally:
        cursor.close()
        conn.close()

@app.delete('/champ/{id}')
async def delete_champ(id:int):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)#conexion con bd
    query = """DELETE FROM "CHAMPIONS" WHERE "CHAMPS_ID" = %s;"""
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