# Ensure the upload directory exists
import os
from flask import Flask
from flask_login import LoginManager

from .db import db
from .models import User
from .routes import main

login_manager = LoginManager()

def create_app(database_uri="sqlite:///IntelliShare.db"):
    app = Flask(__name__, static_url_path='/static')
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = "TOBESETSECRET"


    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    return app