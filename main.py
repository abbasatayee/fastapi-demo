import uvicorn
from fastapi import FastAPI
from src.routes import user_router
from src.utils.config import env_settings as settings


def create_app() -> FastAPI:
    """Initialize the FastAPI app and include routes"""
    # include user-related endpoints from router
    app = FastAPI()
    
    app.include_router(user_router , prefix="/api/v1")
    return app

# include user-related endpoints from router
app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000  , reload=settings.debug)