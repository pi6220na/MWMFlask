from flask import session, redirect, url_for
import MWMFlask.utils.database.connection as db
import MWMFlask.utils.secrets.users as secrets
from MWMFlask.models.users import User
import time


def valid_password(user, password):
    login_qry = "SELECT hash FROM users WHERE email = ?"
    hashed = db.get_rs(login_qry, (user,))[0]
    if secrets.checkpw(password, hashed):
        return True
    return False


def is_unique(email):
    unique_query = "SELECT COUNT(*) FROM users WHERE email = ?"
    rs = db.get_rs(unique_query, (email,))
    if not rs[0]:
        return True
    else:
        return False


def user_exists(email):
    return not is_unique(email)


def get_user(user):
    user_qry = "SELECT email, email_confirmed, admin, first_name, last_name, rowid FROM users WHERE email = ?"
    rs = db.get_rs(user_qry, (user,))
    print(rs)
    db_user = User(db_user=rs)
    return db_user


def login(user, password):
    if valid_password(user, password):
        if user_exists(user):
            db_user = get_user(user)
            start_session(db_user)
            message = "user successfully logged in"
            return {"error": False, "message": message}
        else:
            message = "Invalid username or password"
            return {"error": False, "message": message}
    else:
        message = "Invalid username or password"
        return {"error": False, "message": message}


def start_session(user):
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
    session.clear()
    return {"error": False, "message": "logged out"}
