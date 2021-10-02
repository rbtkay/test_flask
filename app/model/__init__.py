from app.model.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .config import config_by_name

db = SQLAlchemy()

def connect(app):
    db = SQLAlchemy(app)
    return db