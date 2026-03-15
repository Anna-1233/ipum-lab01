# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator
from pydantic import ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        environment = ["dev", "test", "prod"]

        if value not in environment:
            raise ValidationError(f"Invalid environment, must be one of {environment}.")
        else:
            return value
