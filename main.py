from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="public", html=True), name="public")

@app.get("/api")
def home():
    return {"message": "Mindset Of SN Backend Running"}
