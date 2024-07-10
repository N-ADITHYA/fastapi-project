from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_name: str
    database_port: str
    secret_key: str
    time_at_expiration: int
    algorithm: str


    class Config:
        env_file = '.env'

setting = Settings()
