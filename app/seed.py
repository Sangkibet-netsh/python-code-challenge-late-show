from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
from models import Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        # Create episodes
        episode1 = Episode(date='1/11/99', number=1)
        episode2 = Episode(date='1/12/99', number=2)

        # Create guests
        guest1 = Guest(name='Bruce McCulloch', occupation='actor')
        guest2 = Guest(name='Mark McKinney', occupation='actor')

        # Create appearances
        appearance1 = Appearance(rating=5, episode=episode1, guest=guest1)
        appearance2 = Appearance(rating=4, episode=episode1, guest=guest2)
        appearance3 = Appearance(rating=3, episode=episode2, guest=guest1)

        # Add records to the session
        db.session.add_all([episode1, episode2, guest1, guest2, appearance1, appearance2, appearance3])
        
        # Commit the session to the database
        db.session.commit()

if __name__ == '__main__':
    seed_data()
