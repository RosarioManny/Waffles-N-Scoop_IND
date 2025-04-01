from flask import Flask, render_template, redirect, request, session, g, jsonify
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

# <<<<<<<<<<<< ROUTES >>>>>>>>>>>>>>>
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
  # POST
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
  # GET 
  else:
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

# Shop
@app.route("/shop", methods=["GET", "POST"])
def shop():
  if request.method == "POST":
    try:
      data = request.get_json()
      product_id = data["product_id"]
      user_id = session['user_id']
      quantity = data["quantity"]
      print('SHOP QUANT >>', quantity)
      db = get_db()
      # IF SIGNEED IN / USERS
      if user_id:
        # Locate Cart
        cart = db.execute("SELECT id FROM cart WHERE owner_id = ?", (user_id,)).fetchone()
        # print("CART >> ", {cart})
        # CREATE CART IF NONE
        if not cart:
          print("Making cart")
          db.execute("INSERT INTO cart (owner_id) VALUES (?)", (user_id,))
          cart = db.execute("SELECT * FROM cart WHERE owner_id = ?", (user_id,)).fetchone()
          cart_id = cart["id"]
        # GET CART ID
        else:
          print("Already Exists")
          cart_id = cart["id"]
        # ADD TO CART 
        db.execute(
          "INSERT INTO cart_items (cart_id, product_id, quantity) VALUES (?, ?, ?)", 
          (cart_id, product_id, quantity)
        )
        db.commit()
        return jsonify({"success": True, "cart_id": cart_id})
    except Exception as e:
      return jsonify({"DERROR": str(e)}), 500
  else:
    try:
      user_id = session['user_id']
    except:
      user_id = None
    db = get_db()
    #  Get all items
    fetch_ice_cream = db.execute("SELECT * FROM items WHERE category = 'ice_cream'").fetchall()
    fetch_merch = db.execute("SELECT * FROM items WHERE category = 'merchandise'").fetchall()
    fetch_food = db.execute("SELECT * FROM items WHERE category = 'food'").fetchall()
    return render_template("shop.html", user_id=user_id, ice_creams=fetch_ice_cream, merch=fetch_merch, foods=fetch_food) 
  
# Cart
@app.route("/cart", methods=["GET", "POST"])
def cart():
  # EDIT ITEMS IN CART 
  if request.method == "POST":
    return redirect("/cart")
  # GET ROUTE - SHOW ITEMS IN CART
  else:
    try:
      user_id = session["user_id"]
      db = get_db()
      
      if user_id:
        cart = db.execute("SELECT id, owner_id FROM cart WHERE owner_id = ?", (user_id,)).fetchone()
        # print(dict(cart))
        cart_id = cart["id"]
        current_cart_items = db.execute(
          """
          SELECT items.image, items.id, items.name, items.price, CI.quantity as quantity
          FROM items 
          JOIN cart_items AS CI 
          ON items.id = CI.product_id 
          WHERE CI.cart_id = ? 
          GROUP BY items.id
          """, (cart_id,)
          ).fetchall()
        # print(current_cart_items[0]["quantity"])
        subtotal = 0
        for item in current_cart_items:
          # print(dict(item))
          subtotal += (item["price"] * item["quantity"])
        # print(subtotal)
        tax = round(.08 * subtotal, 2)
        total = subtotal + tax
      else:
        user_id = None
      return render_template("cart.html", user_id=user_id, cart_items=current_cart_items, subtotal=subtotal, tax=tax, total=total)
    except: 
      return render_template("cart.html")

# Remove item from cart
@app.route("/cart/remove", methods=["DELETE"])
@login_required
def remove_cart():
  if request.method == "DELETE":
    data = request.get_json()
    product_id = data.get("product_id")
    try:
        user_id = session["user_id"]
        db = get_db()

        # Get the user's cart
        cart = db.execute("SELECT id FROM cart WHERE owner_id = ?", (user_id,)).fetchone()
        if not cart:
            return jsonify({"error": "Cart not found"}), 404
        # Delete Data
        db.execute(
            "DELETE FROM cart_items WHERE cart_id = ? AND product_id = ?",
            (cart["id"], product_id)
        )
        # Save Changes
        db.commit()
        
        # Calculate new total
        cart_items = db.execute("""
            SELECT items.price, COUNT(*) as quantity 
            FROM items 
            JOIN cart_items ON items.id = cart_items.product_id
            WHERE cart_items.cart_id = ?
            GROUP BY items.id
            """, (cart["id"],)).fetchall()
        
        subtotal = 0
        for item in cart_items:
          subtotal += (item["price"] * item["quantity"])
        
        tax = round(0.08 * subtotal, 2)
        total  = subtotal + tax
        
        return jsonify({
            "truth": True,
            "subtotal": subtotal,
            "tax": tax,
            "total": total
        })
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
  return redirect("/cart")
  
@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
  if request.method == "POST":
    user_id = session["user_id"]
    db = get_db()
    data = request.get_json()
    cart_total = data.get("cart_total")
    cart = db.execute("SELECT id FROM cart WHERE owner_id = ?", (user_id,)).fetchone()
    print("CT >> ",cart_total)
    try:
      # CREATE ORDER
      db.execute("INSERT INTO orders (order_total, user_id) VALUES (?, ?)", (cart_total, user_id,))
      #GET THE CREATED ORDER
      order = db.execute("SELECT * FROM orders WHERE user_id = ? ORDER BY id DESC", (user_id,)).fetchone()
      print("ORDER >> ", dict(order))
      # GET ITEMS FROM CART
      cart_items = db.execute("""
            SELECT items.id, items.price, COUNT(*) as quantity 
            FROM items 
            JOIN cart_items ON items.id = cart_items.product_id
            WHERE cart_items.cart_id = ?
            GROUP BY items.id
            """, (cart["id"],)).fetchall()
      # ASSOCIATE ITEMS WITH ORDER
      for item in cart_items:
        db.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?,?, ?)", (order["id"], item["id"], item["quantity"],))
        # DELETE CART ITEMS 
        db.execute("DELETE FROM cart_items WHERE cart_id = ? AND product_id = ?", (cart["id"], item["id"]))
        print("INSERT & DELETED THIS ITEM >>",dict(item))
      db.commit()

      return jsonify({
                "success": True,
                "message": "Checkout complete! Thank you for your purchase.",
                "order_id": order["id"]
            })
    except Exception as e:
      return jsonify({"Error": str(e)}), 500

  return redirect("/cart")

# Profile
@app.route("/profile")
@login_required
def profile():
  user_id = session["user_id"]
  db = get_db()
  user = db.execute("SELECT name, email, description FROM users WHERE id = ?", (user_id,)).fetchone()
  print(user)
  return render_template("profile.html", user_id=user_id, name=user["name"], email=user["email"], description=user["description"] )

# Edit profile
@app.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
  if request.method == "POST":
    user_id = session["user_id"]
    name = request.form.get("name")
    email = request.form.get("email")
    user_description = request.form.get("user_description")
    db = get_db()
    print(email)
    print(name)
    print(user_description)
    db.execute(
      "UPDATE users SET name = ?, email = ?, description = ? WHERE id = ?", 
      (name, email, user_description,  user_id)
    )
    db.commit()
    return redirect("/profile")
    # return render_template("edit_profile.html", name=name, email=email, description=user_description)
  else:
    user_id = session["user_id"]
    db = get_db()
    user = db.execute("SELECT name, email, description FROM users WHERE id = ?", (user_id,)).fetchone()
    print(user)
    return render_template("edit_profile.html", user_id=user_id, name=user["name"], email=user["email"], description=user["description"] )