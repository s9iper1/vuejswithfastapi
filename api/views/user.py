from loguru import logger
from fastapi import APIRouter, Response
from fastapi.responses import ORJSONResponse


stars = {"Bruce Willis": {"movies": ["Die Hard", "Blind Date"]},
         "Arnold Shwarzenegger": {"movies": ["Terminator", "Conan", "Commando"]},
         "Sylvester Stallone": {"movies": ["Rambo", "Cobra", "Over the Top"]}}

app = APIRouter()


@app.get('/fetch', status_code=200)
async def fetch():
    """"return data"""
    logger.info("fetching stars")
    return stars
