"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db, User, Movie, Rating
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def homepage():

    return render_template('homepage.html')

@app.route("/movies")
def movies():

    movies = crud.return_all_movies()
    # query all ratings

    return render_template('all_movies.html', movies=movies, )

@app.route("/movies/<movie_id>")
def show_movie(movie_id):

    movie = crud.get_movie_by_id(movie_id)
    
    return render_template('movie_details.html', movie=movie)

@app.route("/users")
def display_users():

    users = crud.return_all_users()

    return render_template('all_users.html', users=users)

@app.route("/users/<user_id>")
def show_user(user_id):

    user = crud.get_user_profile(user_id)

    return render_template("user_profiles.html", user=user)

@app.route("/users", methods=["POST"])
def create_user():

    email = request.form.get("email")
    password = request.form.get("password")
    output = crud.check_user_email(email)
    new_user = User(email=email, password=password)

    if output != None:
        flash("OH NO, that users email already exists.")
    else:
        flash("Good job you created an account.")
        db.session.add(new_user)
        db.session.commit()

    return redirect("/")

@app.route("/login", methods=["POST"])
def user_login():

    email = request.form.get("email")
    password = request.form.get("password")
    
    user = crud.check_user_email(email)


    if user == None:
        flash("Please create an account.")
    else:
        if crud.get_user_password(email, password) == password:
            flash("You are logged in.")
            session["current_user"] = user.user_id
        else:
            flash("Those passwords don't match.")
    
    return redirect("/")

@app.route("/ratings-form/<movie_id>", methods=["POST"])
def get_ratings(movie_id):

    # 'input[name="garden"]:checked' SYNTAX from the dumb h/w

    rating = request.form.get("rating")
    print("****************************")
    print(rating)

    return redirect("/movies")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
