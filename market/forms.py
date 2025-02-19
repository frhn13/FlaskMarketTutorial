from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="Username:") # Label is what is displayed on webpage
    email_address = StringField(label="Email:")
    password1 = PasswordField(label="Password 1:")
    password2 = PasswordField(label="Password 2:")
    submit = SubmitField(label="Create Account")