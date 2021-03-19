from models.user import UserModel
from models.team import TeamModel
from models.player import PlayerModel

def sample_data(app, db):
    admin = UserModel(email='admin@dev.com', password='secret')
    guest = UserModel(email='guest@dev.com', password='temporary')
    db.session.add(admin)
    db.session.add(guest)

    team1 = TeamModel(name='England')
    team2 = TeamModel(name='Australia')

    db.session.add(team1)
    db.session.add(team2)
    db.session.commit()

    player1a = PlayerModel(name='Jack', team_id=team1.id)
    player1b = PlayerModel(name='Jill', team_id=team1.id)
    db.session.add(player1a)
    db.session.add(player1b)

    player2a = PlayerModel(name='Jamie', team_id=team2.id)
    player2b = PlayerModel(name='James', team_id=team2.id)
    db.session.add(player2a)
    db.session.add(player2b)

    db.session.commit()

