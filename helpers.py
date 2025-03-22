from flask import redirect, session, g
from functools import wraps
import sqlite3

DATABASE = 'database.db'

# Check if user is logged in
def login_required(f):
    @wraps(f)
    def decorator_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorator_function

# Get database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db