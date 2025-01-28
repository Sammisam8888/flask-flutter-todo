from flask import Flask
from .secret import secretkey,db_password
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] = secretkey 
#this is necessary to prevent our website from getting accessed by hackers

app.config["MONGO_URI"] = f"mongodb+srv://sammisam8888:{db_password}@tododb.0apf1.mongodb.net/?retryWrites=true&w=majority&appName=TodoDB"

# setup mongodb
mongodb_client = PyMongo(app)
db=mongodb_client.db

from application import routes

