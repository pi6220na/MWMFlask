from flask import Flask, render_template, request, url_for, redirect, session
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

        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route('/logout', methods=["POST", "GET"])
def logout():
    users.end_session()
    return redirect(url_for("home"))


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        users.create(request.form)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route('/user', methods=["POST", "GET"])
def user():
    return render_template("users.html", title=app.config["APP_TITLE"])


@app.route('/user/update_password', methods=["POST", "GET"])
def update_password():
    if request.method == "POST":
        if "logged_in" in session.keys() and session["logged_in"]:
            print(request.method)
            print(request.form)

            email = session["email"]
            old_pw = request.form["old_password"]
            new_a = request.form["new_password_a"]
            new_b = request.form["new_password_b"]

            if new_a == new_b:
                if users.valid_password(email, old_pw):
                    users.update_password(email, new_a)
                else:
                    print("bad old password")
            else:
                print("didnt match")

            # whatever logic you need to change the password

            return redirect(url_for("user"))
        else:
            return redirect(url_for("home"))
    else:
        return redirect(url_for("user"))


if __name__ == '__main__':
    app.run()
