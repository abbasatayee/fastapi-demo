import uvicorn
from fastapi import FastAPI
from src.routes import v1_router
from src.utils.config import env_settings as settings


def create_app() -> FastAPI:
    """Initialize the FastAPI app and include versioned API routes"""
    app = FastAPI()
    # mount all v1 routers under /api to allow free versioning
    app.include_router(v1_router, prefix="/api")
    return app

# create the app with all configured routers
app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000  , reload=settings.debug)