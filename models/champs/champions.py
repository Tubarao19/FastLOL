from pydantic import BaseModel
from typing import Optional

#se importa pydantic y se crea una clase
#la cual creara un modelo basado en la bd representado en clases de python
class Champ(BaseModel):
    CHAMPS_NAME: str
    CHAMPS_HEALTH: int
    CHAMPS_AD: int
    CHAMPS_AP: int
    CHAMPS_MP: int
    CHAMPS_MANA: int

class Skill(BaseModel):
    SKILL_NAME: str
    SKILL_MANA_COST: int
    CHAMPS_ID: int