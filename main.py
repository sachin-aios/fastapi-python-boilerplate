from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/")
async def home():
    return FileResponse("public/index.html")

@app.get("/api")
async def api():
    return {"message": "Mindset Of SN Running"}
