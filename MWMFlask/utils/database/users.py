from flask import session, redirect, url_for
from MWMFlask.utils.database import connection as db
# import MWMFlask.utils.database.connection as db
import MWMFlask.utils.secrets.users as secrets
from MWMFlask.utils.api import places as places
from MWMFlask.models.users import User
import time


def valid_password(email, password):
    """ tests if the given password given matches the hash in the db for the given user """
    login_qry = "SELECT hash FROM users WHERE email = ?"
    password_rs = db.get_rs(login_qry, (email,))
    print(password_rs)
    print(type(password_rs))
    if password_rs:
        hashed = db.get_rs(login_qry, (email,))[0]
        if secrets.checkpw(password, hashed):
            return True
        else:
            return False
    else:
        return False


def update_password(email, password):
    """ updates the password hash in the db for a given username """
    hashed = secrets.hashpw(password)
    update_qry = "UPDATE users SET hash = ? WHERE email = ?"
    print(hashed)
    db.execute_query(update_qry, (hashed, email))


def is_unique(email):
    """ tests if the new email exists in the db """
    unique_query = "SELECT COUNT(*) FROM users WHERE email = ?"
    rs = db.get_rs(unique_query, (email,))
    if not rs[0]:
        return True
    else:
        return False


def user_exists(email):
    """ tests if the user exists in the db """
    return not is_unique(email)


def get_user(user):
    """ gets user from db and loads into an object """
    user_qry = "SELECT email, email_confirmed, admin, first_name, last_name, user_id FROM users WHERE email = ?"
    rs = db.get_rs(user_qry, (user,))
    db_user = User(db_user=rs)
    return db_user


def login(user, password):
    """ does the login for the givens user and password and returns a success/fail message """
    message = "Invalid username or password"
    if valid_password(user, password):
        if user_exists(user):
            db_user = get_user(user)
            start_session(db_user)
            message = "user successfully logged in"
            return {"error": False, "message": message}
        else:
            return {"error": True, "message": message}
    else:
        return {"error": True, "message": message}


def start_session(user):
    """ loads data from the user into the session vars """
    session["logged_in"] = True
    session["first_name"] = user.first_name
    session["last_name"] = user.last_name
    session["email"] = user.email
    session["user_id"] = user.user_id
    session["admin"] = user.is_admin()
    session["confirmed"] = user.is_confirmed()


def create(form_user):
    email = form_user["email"]
    if is_unique(email):

        first = form_user["first"]
        last = form_user["last"]

        hashed = secrets.hashpw(form_user["password"])
        nonce = secrets.generate_nonce()
        nonce_time = time.time()

        create_qry = "INSERT INTO users (email, first_name, last_name, hash, nonce, nonce_timestamp) " \
                     "VALUES ( ?, ?, ?, ?, ?, ? )"

        db.execute_query(create_qry, (email, first, last, hashed, nonce, nonce_time))
        user = get_user(email)

        start_session(user)
        return {"error": False, "message": "account created"}
    else:
        return {"error": True, "message": "email is taken"}


def end_session():
    """ clears session data and returns a success message """
    session.clear()
    return {"error": False, "message": "User logged out."}


def get_favorites(user_id):
    get_fave_qry = "SELECT place_id FROM favorites WHERE user_id = ?"
    faves = db.get_rs(get_fave_qry, (user_id,))

    favorites = []

    print(faves)

    if len(faves) == 1:
        for f in faves:
            print(f)
            favorites.append(places.get_cached_place_by_id(f))
    elif len(faves) > 1:
        for f in faves:
            print(f[0])
            favorites.append(places.get_cached_place_by_id(f[0]))

    return favorites


def add_favorite(user_id, place_id):
    add_fave_qry = "INSERT INTO favorites (user_id, place_id) VALUES (?, ?)"
    db.execute_query(add_fave_qry, (user_id, place_id))
