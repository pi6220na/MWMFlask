from urllib.request import urlopen
from urllib.error import URLError
from MWMFlask.Main import app
import json
from cachepy import *
from multiprocessing.pool import ThreadPool
import logging


api_key = app.config["WEATHER_DATA_KEY"]

cache_with_ttl = Cache(ttl=60) # ttl given in seconds


def w_forecast():
    '''A simple concurrent threading call'''

    # https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(w_get_forecast)
    return_val = async_result.get()  # get the return value from your function.
    return return_val


def w_current():
    '''A simple concurrent threading call'''

    # https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(w_get_current)
    return_val = async_result.get()  # get the return value from your function.
    return return_val


@cache_with_ttl
@app.route('/w_current', methods=["POST", "GET"])
def w_get_current():
    '''This function calls the weather API to get the current weather condition information.
    The API information is parsed into a JSON string, individual fields are then extracted as needed.'''
    app.jinja_env.globals.update(w_get_current=w_get_current)

    try:
        w_url = "http://api.wunderground.com/api/"
        w_query = "/conditions/q/MN/Minneapolis.json"
        w_req_url = "{}{}{}".format(w_url, api_key, w_query)
        logging.info("Current url: %s" % w_req_url)
        f = urlopen(w_req_url)

    except URLError as e:
        logging.error(e.reason)

    json_string = f.read()
    parsed_json = json.loads(json_string)

    w_curr = []

    # build dictionary entry and append to list
    wc_date_time = parsed_json['current_observation']['observation_time']
    wc_disp_location = parsed_json['current_observation']['display_location']['city']
    wc_lat = parsed_json['current_observation']['display_location']['latitude']
    wc_lon = parsed_json['current_observation']['display_location']['longitude']
    wc_condition = parsed_json['current_observation']['weather']
    wc_condition_url = parsed_json['current_observation']['icon_url']
    wc_temp_f = parsed_json['current_observation']['temp_f']
    wc_heat_index_f = parsed_json['current_observation']['heat_index_f']
    wc_wind_chill_f = parsed_json['current_observation']['windchill_f']
    wc_pressure_in = parsed_json['current_observation']['pressure_in']
    wc_rel_humidity = parsed_json['current_observation']['relative_humidity']
    wc_visibility_mi = parsed_json['current_observation']['visibility_mi']
    wc_wind_dir = parsed_json['current_observation']['wind_dir']
    wc_wind_mph = parsed_json['current_observation']['wind_mph']

    w_curr.append(
            {'wc_date_time':wc_date_time, 'wc_disp_location':wc_disp_location, 'wc_lat':wc_lat, 'wc_lon':wc_lon,
             'wc_condition':wc_condition, 'wc_condition_url':wc_condition_url, 'wc_temp_f':wc_temp_f,
             'wc_heat_index_f':wc_heat_index_f, 'wc_wind_chill_f':wc_wind_chill_f, 'wc_pressure_in':wc_pressure_in,
             'wc_rel_humidity':wc_rel_humidity, 'wc_visibility_mi':wc_visibility_mi, 'wc_wind_dir':wc_wind_dir,
             'wc_wind_mph':wc_wind_mph})
    # close the interface
    f.close()

    logging.debug(w_curr)
    logging.debug('w_current was called, returning to index')
    return w_curr


@cache_with_ttl
@app.route('/w_forecast', methods=["POST", "GET"])
def w_get_forecast():
    '''This function calls the weather API to get the weather forecast information.
    The API information is parsed into a JSON string, individual fields are then extracted as needed.'''
    app.jinja_env.globals.update(w_forecast=w_forecast)

    try:
        w_url = "http://api.wunderground.com/api/"
        w_query = "/forecast/q/MN/Minneapolis.json"
        w_req_url = "{}{}{}".format(w_url, api_key, w_query)
        logging.info("Forecast url: %s" % w_req_url)
        f = urlopen(w_req_url)

    except URLError as e:
        logging.error(e.reason)

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

    logging.debug('w_forecast was called, returning to index')
    return w_fcast



# No caching done here. This is only setting a string. The weather radar gif can't be cached.
@app.route('/w_radar', methods=["POST", "GET"])
def w_radar():
    '''This function sets and returns an animated gif weathter radar to the calling modal.html then index.html'''
    app.jinja_env.globals.update(w_radar=w_radar)

    #radar_url = 'http://api.wunderground.com/api/b27dbdfdaafdef52/radar/image.gif?centerlat=45.0&centerlon=-93.265&radius=100&width=280&height=280&newmaps=1'
    #radar_url = 'http://api.wunderground.com/api/b27dbdfdaafdef52/animatedradar/q/MN/Minneapolis.gif?width=480&height=480&newmaps=1&timelabel=1&timelabel.y=10&num=5&delay=50'

    w_url = "http://api.wunderground.com/api/"
    w_query = "/animatedradar/q/MN/Minneapolis.gif?width=480&height=480&newmaps=1&timelabel=1&timelabel.y=10&num=5&delay=50"
    w_req_url = "{}{}{}".format(w_url, api_key, w_query)
    logging.info("Radar url: %s was set, returning to index" % w_req_url)

    return w_req_url
