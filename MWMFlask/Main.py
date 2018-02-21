from flask import Flask, render_template
import config

app = Flask(__name__)
config_object = config.DevelopmentConfig
app.config.from_object(config_object)


@app.route('/')
def hello_world():
    return render_template("index.html", title=app.config["APP_TITLE"], map_key=app.config["GOOGLE_MAP_KEY"])


if __name__ == '__main__':
    app.run()
