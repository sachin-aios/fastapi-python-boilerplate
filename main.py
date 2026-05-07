from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/", response_class=HTMLResponse)
async def home():
    file_path = os.path.join("public", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api")
async def api():
    return {"message": "Mindset of SN running"}
