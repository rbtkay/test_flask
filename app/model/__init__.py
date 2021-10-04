from app.model.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from .config import config_by_name
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Database:
    connection = SQLAlchemy()

    def __init__(self, app):
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.connection.init_app(app)

    def create_all_tables(self):
        self.connection.create_all()

    @classmethod
    def get_connection(cls):
        return cls.connection
