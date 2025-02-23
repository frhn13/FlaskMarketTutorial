from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError # Adds validation
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check): # FlaskForm knows this function is to validate username
        user = User.query.filter_by(username=username_to_check.data).first()
        if user: # Checks if user already exists with that username
            raise ValidationError("Username already exists! Please try a different username.")

    def validate_email_address(self, email_to_check): # FlaskForm knows this function is to validate email
        user = User.query.filter_by(email_address=email_to_check.data).first()
        if user: # Checks if user already exists with that email
            raise ValidationError("Email already exists! Please try a different email address.")

    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()]) # Label is what is displayed on webpage
    email_address = StringField(label="Email:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password 1:", validators=[Length(min=6, max=30), DataRequired()])
    password2 = PasswordField(label="Password 2:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label="Username:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item!")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item!")