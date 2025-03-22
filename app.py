from flask import Flask, render_template, redirect, url_for, request, session, g,
from flask_session import Session
from helpers import login_required
from config import Config
from models import db
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

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
@app.route("/login", methods=["GET", "POST"])
def login():
  session.clear()

  if request.method == "POST":
    
    if not request.form.get("username"):
      return "Username is Invalid", 400
    elif not request.form.get("password"):
      return "Password is Invalid", 400
  return render_template("login.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.forms.get("username")
    password = request.forms.get("password")
    conf_pwd = request.forms.get("confirmation")
    # Check if field is empty
    if not username or not password or not conf_pwd:
      return ("Invalid Fields", 400)
    # check if password and confirm pwd are the same
    if password != conf_pwd:
      return ("Passwords do not match", 400)
    hashed_password = generate_password_hash(password)
    db
  else:
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