from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr

from typing import List, Optional
from datetime import datetime

# 여기서는 Beer, User 등의 모델 정의를 가져옵니다.
from .beer_models import Beer, SearchResult

# database.py에서 함수를 가져옵니다.
from .database import fetch_beers, insert_beer

app = FastAPI()
app.mount("/", StaticFiles(directory="public", html = True), name="static")

# 새 맥주 정보를 추가합니다.
@app.post("/beers/")
async def create_beer(beer: Beer):
    await insert_beer(beer)
    return {"msg": "Beer data has been stored to database."}

# 모든 맥주 정보를 조회합니다.
@app.get("/beers/", response_model=List[Beer])
async def get_beers():
    beers = await fetch_beers()
    return beers
