import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.email_lookup(data['email']):
            return {"message": "A user with that email already exists"}, 400

        user = UserModel(**data)
        user.save()

        return {"message": "User created successfully."}, 201

class Users(Resource):
     def get(self):
        from pprint import pprint as pp
        pp(UserModel.query.all())
        return {'users': [user.json() for user in UserModel.query.all()]}
