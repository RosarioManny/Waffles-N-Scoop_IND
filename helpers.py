from flask import redirect,request, session, g, jsonify
from functools import wraps
import sqlite3

DATABASE = 'database.db'

# Check if user is logged in
def login_required(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        if session.get("user_id") is None:
            session.clear()
            return redirect("/login")
        return f(*args, **kwargs)
    return decorator_function

# Get database connection
def get_db():
    if not hasattr(g, '_database'):
        g._database = g._database = sqlite3.connect(DATABASE)
        g._database.row_factory = sqlite3.Row
    return g._database

