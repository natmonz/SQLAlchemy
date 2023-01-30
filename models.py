"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def connect_db(app):
    """Connecting to flask app"""
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = 'https://icon-library.com/images/default-user-icon/default-user-icon-13.jpg'

class User(db.Model):
    """Users"""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.Text,
                           nullable=False,
                           unique=True)

    last_name = db.Column(db.Text,
                           nullable=False,
                           unique=True)
    
    image_url = db.Column(db.Text,
                          nullable=False,
                          default=DEFAULT_IMG_URL)

    
