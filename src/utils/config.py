from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool

    class Config:
        env_file = ".env"


env_settings = Settings()