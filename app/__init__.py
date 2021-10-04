from app.admin import init_admin_panel
from app.model.Person import Person
from flask import Flask
from flask_admin.contrib.sqla import ModelView
from .model import Database


app = Flask(__name__)
app.app_context().push()
database = Database(app)
database.create_all_tables()
db = database.connection

init_admin_panel(db)

@app.route('/create')
def create():
    db.create_all()
    return '<h1>Tables created</h1>'

@app.route('/')
def root():
    print(db.get_tables_for_bind())
    return '<h1>Hello world</h1>'

if __name__ == "__main__":
    app.run()