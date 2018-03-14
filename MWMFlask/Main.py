from flask import Flask, render_template, request, url_for, redirect, session, flash
from MWMFlask.models.places import places
from flask_api import status
import config

from urllib.request import urlopen
import json

app = Flask(__name__)
config_object = config.DevelopmentConfig
app.config.from_object(config_object)

from MWMFlask.utils.database import users


@app.route('/')
def home():
    w_icon, w_date, w_conditions = w_forecast()
    return render_template("index.html", title=app.config["APP_TITLE"],
                           places=places, map_key=app.config["GOOGLE_MAP_KEY"],
                           w_icon=w_icon, w_date=w_date, w_conditions=w_conditions)


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


@app.route('/w_forecast', methods=["POST"])
def w_forecast():

    app.jinja_env.globals.update(w_forecast=w_forecast)

    f = urlopen('http://api.wunderground.com/api/b27dbdfdaafdef52/forecast/q/MN/Minneapolis.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)

    w_icon = parsed_json['forecast']['simpleforecast']['forecastday'][0]['icon']
    w_date = parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['weekday']
    w_conditions = parsed_json['forecast']['simpleforecast']['forecastday'][0]['conditions']

    f.close()

    print('w_forecast was called, returning to index')
    return w_icon, w_date, w_conditions

    # return render_template("w_forecast_modal.html", w_icon=w_icon, w_date=w_date, w_conditions=w_conditions)



if __name__ == '__main__':
    app.run()
