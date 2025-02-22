# __init__ makes this directory into package so all variables and functions inside can be imported as if they are from a module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Uniform resource identifier is to identify this as database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = 'aa4b5e9664c20591d44d1696' # Needed to display the form
db = SQLAlchemy(app) # Creates database
bcrypt = Bcrypt(app) # Used for hashing
login_manager = LoginManager(app)
login_manager.login_view = "login_page" # User redirected here if they access page without logging in
login_manager.login_message_category = "info" # Displays error message as info one

from market import routes