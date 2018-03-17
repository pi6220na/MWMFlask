from urllib.request import urlopen
from urllib.error import URLError
from MWMFlask.Main import app
import json
import logging
log = logging.getLogger(__name__)


@app.route('/w_forecast', methods=["POST", "GET"])
def w_forecast():
    '''This function calls the weather API to get the weather forecast information.
    The API information is parsed into a JSON string, individual fields are then extracted as needed.'''
    app.jinja_env.globals.update(w_forecast=w_forecast)

    try:
        f = urlopen('http://api.wunderground.com/api/b27dbdfdaafdef52/forecast/q/MN/Minneapolis.json')
    except URLError as e:
        log.error(e.reason)

    json_string = f.read()
    parsed_json = json.loads(json_string)

    forecast_periods = 2
    w_fcast = []

    # build dictionary entry and append to list
    for x in range(forecast_periods):
        w_date = parsed_json['forecast']['simpleforecast']['forecastday'][x]['date']['pretty']
        w_day = parsed_json['forecast']['simpleforecast']['forecastday'][x]['date']['weekday']
        w_conditions = parsed_json['forecast']['simpleforecast']['forecastday'][x]['conditions']
        w_conditions_url = parsed_json['forecast']['simpleforecast']['forecastday'][x]['icon_url']
        w_high_temp = parsed_json['forecast']['simpleforecast']['forecastday'][x]['high']['fahrenheit']
        w_low_temp = parsed_json['forecast']['simpleforecast']['forecastday'][x]['low']['fahrenheit']
        w_wind_dir = parsed_json['forecast']['simpleforecast']['forecastday'][x]['avewind']['dir']
        w_wind_speed = parsed_json['forecast']['simpleforecast']['forecastday'][x]['avewind']['mph']
        w_avehumidity = parsed_json['forecast']['simpleforecast']['forecastday'][x]['avehumidity']

        w_fcast.append(
            {'w_date': w_date, 'w_conditions': w_conditions, 'w_conditions_url': w_conditions_url,
             'w_high_temp': w_high_temp, 'w_low_temp': w_low_temp, 'w_wind_dir': w_wind_dir,
             'w_wind_speed': w_wind_speed, 'w_avehumidity': w_avehumidity, 'w_day':w_day})
    # close the interface
    f.close()

    log.info('w_forecast was called, returning to index')
    return w_fcast


@app.route('/w_radar', methods=["POST", "GET"])
def w_radar():
    '''This function sets and returns an animated gif weathter radar to the calling modal.html then index.html'''
    app.jinja_env.globals.update(w_radar=w_radar)

    #radar_url = 'http://api.wunderground.com/api/b27dbdfdaafdef52/radar/image.gif?centerlat=45.0&centerlon=-93.265&radius=100&width=280&height=280&newmaps=1'
    radar_url = 'http://api.wunderground.com/api/b27dbdfdaafdef52/animatedradar/q/MN/Minneapolis.gif?width=480&height=480&newmaps=1&timelabel=1&timelabel.y=10&num=5&delay=50'

    log.info(radar_url)
    log.info('w_radar url was set, returning to index')

    return radar_url

