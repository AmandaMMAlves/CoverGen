from fastapi import FastAPI
from app.api import router as cover_router

app = FastAPI()

# Registrando as rotas
app.include_router(cover_router)
