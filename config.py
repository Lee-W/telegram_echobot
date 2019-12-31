import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TOKEN = os.environ.get("TELEGRAM_TOKEN")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    from credentials import TOKEN, SECRET_KEY


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    pass


config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}
