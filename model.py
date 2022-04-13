"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


class Movie(db.Model):
    
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    rating = db.relationship("Rating", back_populates="movie")


    def __repr__(self):
        return f"<Movie: movie_id={self.movie_id} title={self.title}>"
    
class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)

    rating = db.relationship("Rating", back_populates="user")

    def __repr__(self):
        return f'<User: user_id={self.user_id}, Username={self.username}, email={self.email}>'

class Rating(db.Model):
    """"A Ratings"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    movie = db.relationship("Movie", back_populates="rating")
    user = db.relationship("User", back_populates="rating")

    def __repr__(self):
        return f"<Rating: rating_id={self.rating_id}> score={self.score}>"


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
