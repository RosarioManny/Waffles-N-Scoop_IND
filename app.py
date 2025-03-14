from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("Home.html")