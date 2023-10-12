import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    return app
 