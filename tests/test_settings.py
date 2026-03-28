from settings import Settings
from dotenv import load_dotenv


def test_settings():
    load_dotenv("config/.env.test")

    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "APP_test_environment"
    assert settings.API_KEY == "test_password"