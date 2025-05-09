from fastapi import APIRouter
from skills.service_skill import *
from shared.domain.models.champions import Skill

router = APIRouter()

@router.get('/skill')
async def read_skill():
    return await get_skill()

@router.post('/skill')
async def register_skill(skill:Skill):# se crea una variable que almacene lo de pydantic
    return await create_skill(skill)

@router.put('/skill/{id}')
async def refresh_skill(skill:Skill, id:int):
    return await update_skill(skill, id)

@router.delete('/skill/{id}')
async def erase_skill(skill:Skill, id:int):
    return await delete_skill(skill, id)