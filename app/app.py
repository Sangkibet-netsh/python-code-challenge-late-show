#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Episode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    data = [
        {
            'id': episode.id,
            'date': episode.date,
            'number': episode.number
        }
        for episode in episodes
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5555)
