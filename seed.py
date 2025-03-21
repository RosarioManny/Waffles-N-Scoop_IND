from app import app, db
from models import Item

def seed_items():
  with app.app_context():
    db.session.query(Item).delete()