from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(_name_)
    app.config.from_object('config.Config')
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
