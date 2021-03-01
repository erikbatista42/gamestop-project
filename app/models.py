# Create your models here.
from sqlalchemy_utils import URLType

from app import db
# from grocery_app.utils import FormEnum

# class User(db.Model):
#     """User model."""
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     password = db.Column(db.String(200), nullable=False)

class Gamestop(db.Model):
    """Gamestop model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    games = db.relationship('Game', back_populates='gamestop')

class Game(db.Model):
    """Game model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    photo_url = db.Column(URLType)
    
    gamestop_id = db.Column(db.Integer, db.ForeignKey('gamestop.id'), nullable=False)
    gamestop = db.relationship('Gamestop', back_populates='games')