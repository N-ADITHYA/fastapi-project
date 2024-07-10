from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    time_at_expiration: int
    algorithm: str
    database_username: str
    database_password: str
    database_hostname: str
    database_name: str
    database_port: int

    class Config:
        env_file = '.env'

setting = Settings()
