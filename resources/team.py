from flask_restful import Resource, reqparse
from models.team import TeamModel

class Team(Resource):
    def get(self, name):
        team = TeamModel.lookup(name)
        if team:
            return team.json()
        return {'message': 'Team not found'}, 404

    def post(self, name):
        if TeamModel.lookup(name):
            return {'message': "A team with name '{}' already exists.".format(name)}, 400

        team = TeamModel(name)
        try:
            team.save()
        except:
            return {"message": "An error occurred creating the team."}, 500

        return team.json(), 201

    def delete(self, name):
        team = TeamModel.lookup(name)
        if team:
            team.delete()

        return {'message': 'Team deleted'}

class Teams(Resource):
    def get(self):
        return {'teams': [team.json() for team in TeamModel.query.all()]}
