from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the directory that script begins to run
db_path = "sqlite:///" + os.path.join(BASE_DIR, 'sqlite.db')
print db_path
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
db = SQLAlchemy(app)


class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data
      