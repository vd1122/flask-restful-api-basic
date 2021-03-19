import datetime
from db import db
from sqlalchemy import func


class TeamModel(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    code = db.Column(db.String(5))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    players = db.relationship('PlayerModel', back_populates="team", lazy='dynamic')

    def __init__(self, name):
        self.name = name
        self.code = name[:3].upper()

    def json(self):
        return {'id': self.id, 'name': self.name, 'code': self.code, 'players': [player.json() for player in self.players.all()]}

    @classmethod
    def lookup(cls, name):
        return cls.query.filter(func.lower(TeamModel.name)==name.lower()).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
