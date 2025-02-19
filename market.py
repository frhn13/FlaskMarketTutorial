from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # Decorator for webpage URL
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about/<username>") # Page for specific user
def about_page(username):
    return f"<h1>About Page for {username}<h1>"