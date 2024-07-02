from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    time_at_expiration: int
    algorithm: str
    sqlalchemy_db_url: str

    class Config:
        env_file = '.env'

setting = Settings()
