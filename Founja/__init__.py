from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ayo"
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    
    from .main.routes import main

    app.register_blueprint(main)

    return app

