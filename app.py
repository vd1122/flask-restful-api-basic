import os

from flask import Flask
from flask_restful import Api

# from security import authenticate, identity
from flask_sqlalchemy import SQLAlchemy


from resources.user import UserRegister, Users
from resources.team import Team, Teams
from resources.player import Player, Players

from sample_data import sample_data

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'secret'
api = Api(app)

api.add_resource(Teams, '/teams')
api.add_resource(Team, '/team/<string:name>')

api.add_resource(Player, '/player/<string:name>')
api.add_resource(Players, '/players')

api.add_resource(Users, '/users')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
            sample_data(app, db)

    app.run(port=5000)
