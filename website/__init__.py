from os import path
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

db = SQLAlchemy()
DB_NAME = "database.db"
PROTECTED_STRING = "sqlite:///"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = f'{PROTECTED_STRING}{DB_NAME}'
    print(f'{PROTECTED_STRING}{DB_NAME}')

    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_database(app)

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")
