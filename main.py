from fastapi import FastAPI
from champions import control_champs
from skills import control_skill

app = FastAPI()

#se crea la sigt estructura para llamar el contenido de control
app.include_router(control_champs.router, prefix="/api", tags=["Champions"])

app.include_router(control_skill.router, prefix="/api", tags=["Skills"])

"""
fastlol
        -models
                -champions.py
        -services
                -service_champ
                -service_skill
        -controllers
                -control_champ
                -control_skill
        -core
                -config
        -databases
                -connection
                -cursor
        -main

"""