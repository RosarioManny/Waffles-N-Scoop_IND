from flask import Flask, render_template, redirect, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required, get_db
from flask_session import Session
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)

# Session Configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# initialize database
def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
      db.row_factory = sqlite3.Row
    db.commit()

# Close database
@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()


# Home
@app.route("/")
def index():
  # user_id = session["user_id"]
  return render_template("index.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
  # Clears the current session
  session.clear()

  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    # If fields are empty
    if not request.form.get("username"):
      return render_template("login.html", error="Username is Invalid")
    elif not request.form.get("password"):
      return render_template("login.html", error="Password is Invalid")
    
    db = get_db()
    try:
      user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone() #fetchone() >> returns a single row and turns into a dict
      # Grab the userdata and put into a dict(object)
      print(f'LOGGED username: {username}  passwrod: {password}')
    except:
      print(f'ERROR username: {username} VS DBUN: {user} passwrod: {password}')
      return render_template("login.html", error="Field error, please enter again")
    # Check if information is valid
    if user and check_password_hash(user["password"], password):
      print(f'SESSION MADE FOR username: {username} passwrod: {password}')
      session["user_id"] = user["id"]
      return redirect("/")
    else:
      return render_template("login.html", error="Invalid password or username")

  return render_template("login.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    conf_pwd = request.form.get("confirmation")

    print(f"Username: {username}, Password: {password}, Confirm Password: {conf_pwd}")
    # Check if field is empty
    if not username or not password or not conf_pwd:
      return ("Invalid Fields", 400)
    # check if password and confirm pwd are the same
    if password != conf_pwd:
      return ("Passwords do not match", 400)
    hashed_password = generate_password_hash(password)
    db = get_db()

    try:
      db.execute("INSERT INTO users (username, password) VALUES(?, ?)",(username, hashed_password))
      db.commit()
    # Error Handling
    except sqlite3.IntegrityError as e:
      print(f"IntegrityError: {e}")
      return render_template("register.html", error="Username already exists")
    except Exception as e:
      print(f"Unexpected error: {e}")
      return render_template("register.html", error="An error occurred. Please try again.")
    # If successful go to login
    return redirect("/login")
  else:
    return render_template("register.html")

# Logout
@app.route("/logout")
def logout():

  session.clear()

  return redirect("/")
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

@app.route("/shop")
def shop():
  return render_template("shop.html")