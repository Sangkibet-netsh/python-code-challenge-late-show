#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse

from models import db, Episode,Appearance,GuestS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class EpisodeResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        data = [
            {
                'id': episode.id,
                'date': episode.date,
                'number': episode.number
            }
            for episode in episodes
        ]
        return data


if __name__ == '__main__':
    app.run(port=5555)
