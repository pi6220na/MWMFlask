from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_api import status
import config

app = Flask(__name__)
config_object = config.DevelopmentConfig
app.config.from_object(config_object)

from MWMFlask.utils.database import users


@app.route('/')
def home():
    return render_template("index.html", title=app.config["APP_TITLE"], map_key=app.config["GOOGLE_MAP_KEY"])


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        users.login(request.form["email"], request.form["password"])
        return redirect(url_for("home")), status.HTTP_200_OK
    else:
        return redirect(url_for("home")), status.HTTP_401_UNAUTHORIZED


@app.route('/logout', methods=["POST", "GET"])
def logout():
    users.end_session()
    return redirect(url_for("home")), status.HTTP_200_OK


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        users.create(request.form)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home")), status.HTTP_405_METHOD_NOT_ALLOWED


@app.route('/user', methods=["POST", "GET"])
def user():
    return render_template("users.html", title=app.config["APP_TITLE"]), status.HTTP_200_OK


@app.route('/user/update_password', methods=["POST", "GET"])
def update_password():
    if request.method == "POST":
        if "logged_in" in session.keys() and session["logged_in"]:
            email = session["email"]
            old_pw = request.form["old_password"]
            new_a = request.form["new_password_a"]
            new_b = request.form["new_password_b"]

            if new_a == new_b:
                if users.valid_password(email, old_pw):
                    users.update_password(email, new_a)
                else:
                    flash("The old password did not match")
                    return redirect(url_for("user")), status.HTTP_401_UNAUTHORIZED
            else:
                flash("The new passwords did not match")
                return redirect(url_for("user")), status.HTTP_400_BAD_REQUEST
            return redirect(url_for("user")), status.HTTP_200_OK
        else:
            return redirect(url_for("home")), status.HTTP_401_UNAUTHORIZED
    else:
        return redirect(url_for("user")), status.HTTP_405_METHOD_NOT_ALLOWED


if __name__ == '__main__':
    app.run()
