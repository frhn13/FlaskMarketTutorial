from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired # Adds validation

class RegisterForm(FlaskForm):
    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()]) # Label is what is displayed on webpage
    email_address = StringField(label="Email:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password 1:", validators=[Length(min=6, max=30), DataRequired()])
    password2 = PasswordField(label="Password 2:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")