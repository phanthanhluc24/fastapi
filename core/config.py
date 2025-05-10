from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    database_test_url: str
    email_sender: str
    email_password: str
    email_smtp_host: str
    email_smtp_port: str
    class Config:
        env_file = ".env"

settings = Settings()
