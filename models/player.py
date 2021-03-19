from db import db
import datetime
from sqlalchemy import func

class PlayerModel(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    debut = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team = db.relationship('TeamModel', back_populates="players")

    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id

    def json(self):
        return {'id': self.id, 'name': self.name, 'debut': str(self.debut.strftime("%b %d %Y"))}

    @classmethod
    def lookup(cls, name):
        return cls.query.filter(func.lower(PlayerModel.name)==name.lower()).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
