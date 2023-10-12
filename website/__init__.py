import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite: ///{DB_NAME}"
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_perfix="/")
    app.register_blueprint(auth, url_perfix="/")

    return app
