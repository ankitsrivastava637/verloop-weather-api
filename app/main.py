import logging
from fastapi import FastAPI
from app.routers.weather import router as weather_router
import uvicorn

logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(weather_router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
