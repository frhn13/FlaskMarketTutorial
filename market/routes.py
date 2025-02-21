from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route("/") # Decorator for webpage URL
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
@login_required # Can't access page unless logged in
def market_page():
    items = Item.query.all() # Items includes all entered items
    return render_template("market.html", items=items)

@app.route("/about/<username>") # Page for specific user
def about_page(username):
    return f"<h1>About Page for {username}<h1>"

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        # item_to_create = Item(name="Steve", price=12.50, barcode="123412341234", description="Image of Steve")
        # db.session.add(item_to_create)
        db.session.commit()
        login_user(user_to_create) # Logs in created user
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category="success")
        return redirect(url_for("market_page"))
    if form.errors != {}: # If no validation errors
        for err_message in form.errors.values():
            flash(f"There was an error with the user {err_message}", category="danger") # Shows error message in danger category
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first() # Checks if user exists
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user) # Checks if password matches hashed password
            flash(f"Success! You are logged in as: {attempted_user.username}", category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Username and password are not matching! Please try again.", category="danger")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user() # Logs out current user and clear their session data
    flash("You have been logged out.", category="info")
    return redirect(url_for("home_page")) # Returns them to homepage
