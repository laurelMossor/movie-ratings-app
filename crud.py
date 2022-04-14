"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )

    return movie

def return_all_movies():

    # Returns a list of Movie objects
    list_of_movies = Movie.query.all()

    return list_of_movies

def get_movie_by_id(x_movie_id):

    return Movie.query.filter_by(movie_id=x_movie_id).one()

def return_all_users():

    return User.query.all()

def get_user_profile(x_user_id):

    return User.query.filter_by(user_id=x_user_id).one()

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
