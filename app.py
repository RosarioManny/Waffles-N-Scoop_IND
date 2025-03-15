from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html")
@app.route("/cart")
def cart():
  return render_template("cart.html")

@app.route("/profile")
def profile():
  return render_template("profile.html")