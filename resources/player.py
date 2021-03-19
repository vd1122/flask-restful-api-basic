from flask_restful import Resource, reqparse
from models.player import PlayerModel

class Player(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('team_id',
        type=int,
        required=True,
        help="Every player needs a team id."
    )

    def get(self, name):
        player = PlayerModel.lookup(name)
        if player:
            return player.json()
        return {'message': 'Player not found'}, 404

    def post(self, name):
        if PlayerModel.lookup(name):
            return {'message': "A player with name '{}' already exists.".format(name)}, 400

        data = Player.parser.parse_args()

        player = PlayerModel(name, **data)

        try:
            player.save()
        except:
            return {"message": "An error occurred inserting the player."}, 500

        return player.json(), 201

    def delete(self, name):
        player = PlayerModel.lookup(name)
        if player:
            player.delete()

        return {'message': 'Player deleted'}

    def put(self, name):
        data = Player.parser.parse_args()

        player = PlayerModel.lookup(name)

        if player is None:
            player = PlayerModel(name, **data)

        player.save()

        return player.json()


class Players(Resource):
    def get(self):
        return {'players': [player.json() for player in PlayerModel.query.all()]}
