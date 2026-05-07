from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/", response_class=HTMLResponse)
async def home():
    file_path = os.path.join("public", "index.html")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>404 - Index file not found</h1>"
    except Exception as e:
        return f"<h1>Error reading file: {str(e)}</h1>"

@app.get("/api")
async def api():
    return {"message": "Mindset of SN running"}
