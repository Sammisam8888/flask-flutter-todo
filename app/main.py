from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo-app.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)
ma=Marshmallow(app)

@app.route('/')
def hello():
    return "Home Page"

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    is_executed = db.Column(db.Boolean)

    def __init__(self, name, is_executed):
        self.name = name
        self.is_executed = is_executed


# Todo schema
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'is_executed')


# Initialize schema
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
