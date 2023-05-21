# import asyncio
from fastapi import FastAPI, Query, Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from models import Beer, UserFavorites
from database import find_all_beers, find_beer, find_user_favorites
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

app = FastAPI()
app.mount("/", StaticFiles(directory="public", html = True), name="static")

# 모든 맥주 정보를 조회합니다.  ex) /beers/all

@app.get("/beers/all")
async def get_all_beers():
    # from motor.motor_asyncio import AsyncIOMotorClient
    # import os
    # password = os.environ.get("MONGODB_PWD")
    # uri = f"mongodb+srv://admin:{password}@recommend.wg2l4em.mongodb.net/?retryWrites=true&w=majority"
    # db = AsyncIOMotorClient(uri).BeerRecommendationsDB
    # beers = db.Beers
    # beer_list = await beers.find().to_list(length=1000)
    return "hello world"


# @app.get("/beers/all", response_model=List[Beer])
# async def get_all_beers():
#     result = await find_all_beers()
#     return result

# 모든 맥주 정보를 조회합니다.  ex) /beers/all

# @app.get("/beers/all", response_model=List[Beer])
# async def get_all_beers():
#     from motor.motor_asyncio import AsyncIOMotorClient
#     import os
#     password = os.environ.get("MONGODB_PWD")
#     uri = f"mongodb+srv://admin:{password}@recommend.wg2l4em.mongodb.net/?retryWrites=true&w=majority"
#     client = AsyncIOMotorClient(uri)
#     # 데이터베이스를 선택합니다.
#     db = client.BeerRecommendationsDB
#     beers = db.Beers
#     beer_list = await beers.find().to_list(length=1000)
#     return beer_list

# import asyncio
# beer_list = asyncio.run(get_all_beers())
# print(beer_list)


# 맥주 정보를 조회합니다.   ex) /beers?beer_name=cass
@app.get("/beers/", response_model=Beer)
async def get_beer_by_name(beer_name: str = Query(...)):
    result = await find_beer(beer_name)
    return result

# 찜한 정보를 조회합니다.   ex) /userfavorites?user_id=user1
@app.get("/userfavorites/", response_model=UserFavorites)
async def get_user_favorites(user_id: str = Query(...)):
    result = await find_user_favorites(user_id)
    return result

# 찜한 맥주를 추가합니다.   ex) /userfavorites?user_id=user1&beer_id=beer123
@app.post("/userfavorites/", response_model=UserFavorites)
async def add_favorite_beer(user_id: str = Query(...), beer_id: str = Query(...)):
    result = await add_favorite_beer(user_id, beer_id)
    return result

# 이미지 파일 반환하기 ex) /data/img/카스.jpg
@app.get("/data/img/{filename}")
async def get_image(filename: str = Path(...)):
    return FileResponse(path=f"data/img/{filename}", media_type="image/jpeg")