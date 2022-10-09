from fastapi import FastAPI
from app.routes import(file)
app = FastAPI()
app.include_router(file.router)
@app.get("/")
async def check_health() -> str:
    return "Health OK"