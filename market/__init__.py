# __init__ makes this directory into package so all variables and functions inside can be imported as if they are from a module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Uniform resource identifier is to identify this as database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
db = SQLAlchemy(app) # Creates database

from market import routes