from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route('/')
def hello_world():
    return render_template("index.html", title=app.config["APP_TITLE"], map_key=app.config["MAP_KEY"])


if __name__ == '__main__':
    app.run()
