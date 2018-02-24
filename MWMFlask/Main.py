from flask import Flask, render_template, request, url_for, redirect
from MWMFlask.utils.database import users
# import MWMFlask.utils.database as db
import config

app = Flask(__name__)
config_object = config.DevelopmentConfig
app.config.from_object(config_object)


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


if __name__ == '__main__':
    app.run()
