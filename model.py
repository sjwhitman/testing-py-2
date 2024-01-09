from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #write a function that creates a game and adds it to the database.
    #create the test game
    game = Game(game_id= 200, name='Potato Game', description='Potatoes are ruling the world')
    
    #add test game to db
    db.session.add(game)
    db.session.commit()

    print("The data we added to the DB")


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
