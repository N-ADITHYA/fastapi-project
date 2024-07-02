from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_name: str
    database_username: str
    database_port: str
    database_password: str
    database_hostname: str
    secret_key: str
    time_at_expiration: int
    algorithm: str
    sqlalchemy_db_url: str

    class Config:
        env_file = '.env'

setting = Settings()
