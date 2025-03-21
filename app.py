from flask import Flask, render_template, redirect, url_for, request, session, g
from flask_session import Session
from helpers import login_required
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all() 

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# Home
@app.route("/")
def hello_world():
  return render_template("home.html")

# Login
@app.route("/login")
def login():
  return render_template("login.html")

# Register
@app.route("/register")
def register():
  return render_template("register.html")

# About
@app.route("/about")
def about():
  return render_template("about.html")

# Cart
@app.route("/cart")
def cart():
  return render_template("cart.html")

# Profile
@app.route("/profile")
@login_required
def profile():
  return render_template("profile.html")

# History
@app.route("/history")
@login_required
def history():
  return render_template("history.html")