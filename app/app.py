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
    
class SingleEpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            data = {
                'id': episode.id,
                'date': episode.date,
                'number': episode.number,
                'guests': [
                    {
                        'id': appearance.guest.id,
                        'name': appearance.guest.name,
                        'occupation': appearance.guest.occupation
                    }
                    for appearance in episode.appearances
                ]
            }
            return data
        else:
            return {'error': 'Episode not found'}, 404

    def delete(self, id):
        episode = Episode.query.get(id)
        if episode:
            db.session.delete(episode)
            db.session.commit()
            return '', 204
        else:
            return {'error': 'Episode not found'}, 404
class GuestResource(Resource):
    def get(self):
        guests = Guest.query.all()
        data = [
            {
                'id': guest.id,
                'name': guest.name,
                'occupation': guest.occupation
            }
            for guest in guests
        ]
        return data


if __name__ == '__main__':
    app.run(port=5555)
