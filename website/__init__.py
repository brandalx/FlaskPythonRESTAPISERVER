import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_perfix="/")
    app.register_blueprint(auth, url_perfix="/")

    return app
