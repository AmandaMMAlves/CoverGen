import requests
from dotenv import load_dotenv
import os 
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_cover_image(album_name: str, description: str, genre: str, style: str) -> str:
    try:
        # Fazendo a requisição para a API de IA

        response = client.images.generate(
            prompt=f"Album cover for an album named '{album_name}' with the following description: '{description}'. The genre is '{genre}' and the style is '{style}'.",
            n=1,
            size="1024x1024",
            model="dall-e-2",
            quality="hd"
        )

        # Extraindo o URL da imagem gerada
        return response.data[0].url
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao chamar a API de IA: {str(e)}")
