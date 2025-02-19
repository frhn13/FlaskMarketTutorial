from market import app
from flask import render_template
from market.models import Item

@app.route("/") # Decorator for webpage URL
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market():
    items = Item.query.all() # Items includes all entered items
    return render_template("market.html", items=items)

@app.route("/about/<username>") # Page for specific user
def about_page(username):
    return f"<h1>About Page for {username}<h1>"