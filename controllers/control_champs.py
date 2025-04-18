from fastapi import APIRouter
from services.service_champs import get_champs, create_champ
from models.champions import Champ 

router = APIRouter()

@router.get('/champs')
async def read_champs():
    return await get_champs()# se usa await para la espera de una funcion asincrona


@router.post('/champ')
async def register_champ(champ:Champ): #se llama el modelo de pydantic y se pasa como parametro
    return await create_champ(champ)#con el fin de pasar los datos de forma estructurada