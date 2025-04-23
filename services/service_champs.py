from fastapi import HTTPException
from databases.cursor import execute_query
from models.champions import Champ
import psycopg2

#READ
async def get_champs():
    query = 'SELECT * FROM "CHAMPIONS";'
    try:
        return execute_query(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar campeones: {e}")
    

#CREATE
async def create_champ(champ:Champ):# se crea una variable que almacene lo de pydantic
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
        champ_info = execute_query(query, values)
        if champ_info: #se almacena en una variable champ_info los datos a enviar
            champ_data = champ_info[0] #se retorna la informacion mandada a la bd
            return {"message":"Champ agregado correctamente", "CHAMPS_ID":champ_data, "CHAMPS_NAME":champ_data} 
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    

#UPDATE
async def update_champ(champ:Champ, id:int):
    query = """UPDATE "CHAMPIONS"
            SET "CHAMPS_NAME" = %s,
                "CHAMPS_AD" = %s,
                "CHAMPS_HEALTH" = %s,
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
        returning = execute_query(query, values)
        if not returning:#sino devuelve dato alguno
            raise HTTPException(status_code=404, detail=f"Error champion no encontrado.")
        champion = returning[0]#en caso que devuelva info la base de datos
        return {"message":"Champ actualizado correctamente",
                "update_data": champion}#muestra todos los datos que fueron cambiados
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error en algun dato a guardar del champion:{e}")
    
#DELETE
async def delete_champ(id:int):
    query = """DELETE FROM "CHAMPIONS" WHERE "CHAMPS_ID" = %s RETURNING "CHAMPS_NAME";"""
    values = (id) 
    try:
        status_champ = execute_query(query, values)
        if not status_champ:
            raise HTTPException(status_code=404, detail=f"Error champion no encontrado.")
        del_champ = status_champ[0]
        return {"message":f"El usuario {del_champ["CHAMPS_NAME"]} fue eliminado correctamente"}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error en algun dato a eliminar del champion:{e}")