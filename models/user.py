import datetime
import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(15))
    password = db.Column(db.String(20))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def json(self):
        return {'id': self.id, 'email': self.email}

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def email_lookup(cls, email):
        return cls.query.filter_by(email__iexact=email).first()

    @classmethod
    def id_lookup(cls, _id):
        return cls.query.filter_by(id=_id).first()
