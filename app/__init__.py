from app.model.Person import Person
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .model import connect

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = connect(app)


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='Msp', template_mode='bootstrap3')
admin.add_view(ModelView(Person, db.session))
# admin.add_view(ModelView(Person), db.session)

@app.route('/')
def root():
    return '<h1>Hello world</h1>'

if __name__ == "__main__":
    app.run()