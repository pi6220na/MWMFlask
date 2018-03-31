import requests
import math
from MWMFlask.models.places import *
from MWMFlask.Main import app
import MWMFlask.utils.database.connection as db
from MWMFlask.models.places import type_strings
import logging


def build_request(request_url, api_route, query_string):
    """ Combines parts of a request url"""
    return "{}{}{}".format(request_url, api_route, query_string)


def get_places(location, radius):
    """ gets places from google in radius of lat and lng """
    queried_places = []
    for t in places:
        qp = google_places_request(location, radius, t.types[0])
        print(qp)
        for p in qp:
            queried_places.append(p)
    return queried_places


def get_cached_by_radius(location: tuple, search_radius) -> list:
    """ This function was adapted from:
    https://stackoverflow.com/questions/21042418/mysql-select-coordinates-within-range
    """
    qry_args = (location[0], location[1], location[0], search_radius/1000)

    # sqlite dose not have all the same math functions as mysql
    # this is a list of python functions tp pass along to sqlite
    functions = (
        ("ACOS", 1, math.acos),
        ("COS", 1, math.cos),
        ("SIN", 1, math.sin),
        ("RADIANS", 1, math.radians)
    )

    # this sql call is what I took from the site, it finds all
    get_places_in_radius_qry = "SELECT *, ( 3959 * ACOS( COS( RADIANS(?) )" \
                               " * COS( radians( latitude ) ) * COS( RADIANS( longitude ) " \
                               "- RADIANS(?) ) + SIN( RADIANS(?) ) * SIN( RADIANS( latitude ) ) ) ) " \
                               "AS distance FROM cache WHERE distance < ?"

    search_rs = db.get_rs(get_places_in_radius_qry, qry_args, custom_functions=functions)

    cached_places = places_from_search_results(search_rs)

    return cached_places


def places_from_search_results(search_rs):
    logging.debug("tuning places query into place objects")
    cached_places = []
    for row in search_rs:
        created = row[1]
        place_id = row[2]
        name = row[3]

        lat = row[4]
        lng = row[5]

        address = row[6]

        types = get_types_by_place_id(place_id)

        location = {'lat': lat, 'lng': lng}

        queried_place = Place(place_name=name, place_id=place_id, location=location,
                              address=address, place_types=types, created=created)

        cached_places.append(queried_place)
    return cached_places


def google_places_request(location: (float, float), radius: int, place_type: str):
    logging.debug("Getting places from google places")

    places_of_type = []

    user_lat = location[0]
    user_lng = location[1]

    search_rad = radius

    api_key = app.config["GOOGLE_MAP_KEY"]

    pl_type = place_type

    pl_url = "https://maps.googleapis.com/"
    pl_route = "maps/api/place/nearbysearch/"
    pl_query = "json?location={},{}&radius={}&type={}&key={}".format(user_lat, user_lng, search_rad, pl_type, api_key)

    places_req_url = build_request(pl_url, pl_route, pl_query)

    response = requests.get(places_req_url)

    results = response.json()["results"]

    for place in results:
        coordinates = dict(place["geometry"]["location"])

        place_name = place["name"]

        place_address = place["vicinity"]

        place_id = place["place_id"]

        types = place["types"]

        place_obj = Place(place_name=place_name, place_id=place_id, location=coordinates, place_types=types,
                          address=place_address)

        places_of_type.append(place_obj)

    return set(places_of_type)


def get_places_by_id(expired):
    refreshed = []
    for place in expired:
        refreshed.append(get_place_by_id(place.place_id))
    return refreshed


def get_place_by_id(expired_place_id):

    api_key = app.config["GOOGLE_MAP_KEY"]

    pl_url = "https://maps.googleapis.com/"
    pl_route = "maps/api/place/details/"
    pl_query = "json?placeid={}&key={}".format(expired_place_id, api_key)

    request_str = build_request(pl_url, pl_route, pl_query)

    resp = requests.get(request_str).json()["result"]

    name = resp["name"]
    place_id = resp["place_id"]
    address = resp["vicinity"]
    location = resp["geometry"]["location"]
    types = resp["types"]

    return Place(place_name=name, place_id=place_id, location=location, address=address, place_types=types)


def get_place_from_db_line(rs_line: tuple) -> Place:

    place_name = rs_line[3]
    place_id = rs_line[2]
    location = (rs_line[4], rs_line[5])
    address = rs_line[6]
    created = rs_line[1]

    type_list = get_types_by_place_id(place_id)

    return Place(place_name=place_name, place_id=place_id, location=location, address=address, place_types=type_list,
                 created=created)


def get_types_by_place_id(place_id: str) -> [str]:
    place_types_by_id_qry = """
    SELECT DISTINCT pt.place_type
        FROM place_types as pt
        JOIN cached_type as ct ON ct.type_id = pt.type_id
        JOIN cache as c ON c.place_id = ct.place_id
    WHERE c.place_id = ?"""
    place_rs = db.get_rs(place_types_by_id_qry, (place_id,))
    type_list = []
    for r in place_rs:
        if isinstance(r, tuple):
            type_list.append(r[0])
        else:
            type_list.append(r)
    return type_list


def update_expired_place(place: Place):

    args = (place.name, place.latitude, place.longitude, place.address, place.created)

    update_qry = """
    UPDATE cache
        SET name = ?, latitude = ?, longitude = ?, address = ?, cached_stamp = ?
        WHERE place_id = ? """
    db.execute_query(update_qry, args)


def build_cache(location: tuple, radius: int):
    place_list = get_places(location, radius)
    for p in place_list:
        new_qry = "INSERT INTO cache (name, place_id, latitude, longitude, address) VALUES (?, ?, ?, ?, ?)"
        db.execute_query(new_qry, p.get_database_args())

        new_type_qry = "INSERT INTO cached_type (place_id, type_id) VALUES (?, ?)"

        for t in p.types:
            if t in type_strings:
                t_id = type_strings.index(t) + 1
                db.execute_query(new_type_qry, (p.place_id, t_id))


if __name__ == '__main__':
    pass
