from ensurepip import bootstrap
from flask import Blueprint, Flask
main = Blueprint('main',__name__)
from . import views


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
