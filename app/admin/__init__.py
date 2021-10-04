from app.model.Person import Person
from flask_admin.base import Admin
from flask_admin.contrib.sqla.view import ModelView
from flask import current_app


def init_admin_panel(db):
    current_app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(current_app, name='Msp', template_mode='bootstrap3')
    admin.add_view(ModelView(Person, db.session))
