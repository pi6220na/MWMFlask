from urllib.request import urlopen
from MWMFlask.Main import app
import json
# import logging
# log = logging.getLogger(__name__)




@app.route('/w_forecast', methods=["POST", "GET"])
def w_forecast():

    app.jinja_env.globals.update(w_forecast=w_forecast)

    f = urlopen('http://api.wunderground.com/api/b27dbdfdaafdef52/forecast/q/MN/Minneapolis.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)

    w_icon = parsed_json['forecast']['simpleforecast']['forecastday'][0]['icon']
    w_date = parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['weekday']
    w_conditions = parsed_json['forecast']['simpleforecast']['forecastday'][0]['conditions']

    f.close()

    # log.info('w_forecast was called, returning to index')
    return w_icon, w_date, w_conditions


@app.route('/w_radar', methods=["POST", "GET"])
def w_radar():

    app.jinja_env.globals.update(w_radar=w_radar)

    w_mplsRadar = 'http://api.wunderground.com/api/b27dbdfdaafdef52/radar/image.gif?centerlat=45.0&centerlon=-93.265&radius=100&width=280&height=280&newmaps=1'

    print(w_mplsRadar)

    # log.info('w_radar was called, returning to index')
    return w_mplsRadar

