from fastapi import HTTPException
from shared.infra.db.cursor import execute_query
from shared.domain.models.champions import Skill
import psycopg2


async def get_skill():
    query = 'SELECT * FROM "SKILLS";'

    try:
        return execute_query(query) #mostrar dichos datos almacenados
    except psycopg2.Error as err:#error al ejecutar el intento
        raise HTTPException(status_code=500, detail=f"error al conectar con postgres: {err}")
    

async def create_skill(skill:Skill):# se crea una variable que almacene lo de pydantic
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
        skill_info = execute_query(query, values)
        if skill_info:#si devuelve un query en formato json lleno
            skill_data = skill_info[0]
        return {"message":"nueva habilidad agregada correctamente", "SKILL_ID":skill_data, "SKILL_NAME":skill_data}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")
    


async def update_skill(skill:Skill, id:int):
    query = """UPDATE "SKILLS"
    SET "SKILL_NAME" = %s,
    "SKILL_MANA_COST" = %s,
    "CHAMPS_ID" = %s
    WHERE "SKILL_ID" = %s RETURNING "SKILL_ID", "SKILL_NAME";"""
    
    values = (skill.SKILL_NAME,
            skill.SKILL_MANA_COST,
            skill.CHAMPS_ID,
            id)
    
    try:
        skill_info = execute_query(query, values)
        if not skill_info:
            raise HTTPException(status_code=404, detail="Error habilidad no encontrada")
        skill_update = skill_info[0]
        return {"message":"habilidad actualizada correctamente",
                "update_data": skill_update}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al agregar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a guardar del champion:{e}")

async def delete_skill(skill:Skill, id:int):
    query = """DELETE FROM "SKILLS" WHERE "SKILL_ID" = %s RETURNING "SKILL_ID", "SKILL_NAME";"""
    values = (id) 

    try:
        skill_info = execute_query(query, values)
        if not skill_info:
            raise HTTPException(status_code=404, detail="Error habilidad no encontrada")
        skill_delete = skill_info[0]
        return {"message":"usuario eliminado correctamente",
                "delete_data": skill_delete}
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el champion: {err}")
    except ValueError as e:#se usa cuando hubo un error de un dato digitado sea por el tipo
        raise HTTPException(status_code=403, detail=f"Error al en algun dato a eliminar del champion:{e}")