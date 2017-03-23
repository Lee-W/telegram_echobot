from flask import Flask
from flask_bootstrap import Bootstrap
import telegram

from config import config


bot = None
bootstrap = Bootstrap()


def create_app(config_name):
    global bot

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bot = telegram.Bot(config[config_name].TOKEN)
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
