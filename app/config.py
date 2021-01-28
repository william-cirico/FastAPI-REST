from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = 'sqlite:///./db.sqlite3'
    sqlalchemy_testing_database_url: str = 'sqlite:///./test_db.sqlite3'

    class Config:
        env_file = '.env'


settings = Settings()
