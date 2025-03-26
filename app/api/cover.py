from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import generate_cover_image

router = APIRouter(prefix="/api/cover", tags=["covers"])

# Definindo o modelo para as entradas
class CoverRequest(BaseModel):
    album_name: str
    description: str
    genre: str
    style: str

@router.post("/")
async def generate_cover(cover: CoverRequest):
    try:
        # Chama o serviço que gera a capa
        image_url = await generate_cover_image(cover.album_name, cover.description, cover.genre, cover.style)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar a capa: {str(e)}")
