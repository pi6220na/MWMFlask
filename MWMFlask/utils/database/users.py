import MWMFlask.utils.database.connection as db
import MWMFlask.utils.secrets.users as secrets


def valid_password(user, password):
    login_qry = "SELECT hash FROM users WHERE email = ?"
    hashed = db.get_rs(login_qry, (user,))[0]
    if secrets.checkpw(password, hashed):
        return True
    return False


def get_user(user):
    user_qry = "SELECT email, email_confirmed, admin, first_name, last_name, rowid FROM users WHERE email = ?"
    rs = db.get_rs(user_qry, (user,))
    print(rs)
    pass


def login(user, password):
    if valid_password(user, password):
        db_user = get_user(user)
        return db_user
    return None

