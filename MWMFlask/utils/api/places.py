from MWMFlask.utils.api import calls
from MWMFlask.models.places import Place
from flask import jsonify
from MWMFlask.utils.database import connection as db
from multiprocessing.pool import ThreadPool
import logging


def call_get_cached(location: tuple, place_types: [str], radius: int):

    # https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(get_cached, [location, place_types, radius])

    return_val = async_result.get()  # get the return value from your function.
    return return_val


def get_cached(location: tuple, place_types: [str], radius: int):
    logging.debug("Getting cached places...")

    cached = calls.get_cached_by_radius(location=location, search_radius=radius)
    expired = check_for_expired(cached)

    if len(expired) > 0:
        refreshed = calls.get_places_by_id(expired)
        update_records(refreshed)

    pl_list = []

    for t in place_types:
        pl_list.extend([pl for pl in cached if t in pl.types])

    return pl_list


def check_for_expired(cached: [Place]) -> [Place]:
    logging.debug("Checking for expired places...")

    expired = []
    for record in cached:
        if record.cache_expired():
            expired.append(record)
    return expired


def update_records(refreshed: [Place]) -> None:
    logging.debug("Updating cache...")

    for place in refreshed:
        calls.update_expired_place(place)


def parse_request_types(types: str):
    logging.debug("parsing tyoes")
    parsed_types = []
    if '-' in types:
        parsed_types = types.split("-")
    else:
        parsed_types.append(types)
    return parsed_types


def update_cache(location, radius):
    logging.debug("Updating cache...")
    calls.build_cache(location, radius)
    return jsonify({'error': False, 'message': 'Cache has been updated'})


def get_cached_place_by_id(place_id: str) -> Place:
    logging.debug("Getting places by id")
    cached_qry = "SELECT * FROM cache WHERE place_id = ?"
    rs = db.get_rs(cached_qry, (place_id,))

    location = (rs[4], rs[5])
    types = get_types_by_place_id(rs[2])

    return Place(rs[3], rs[2], location, rs[6], types)


def get_types_by_place_id(place_id: str) -> [str]:
    logging.debug("geting place tyoes by id")
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


if __name__ == '__main__':
    # print(get_cached_place_by_id("ChIJL_d7hr8ts1IRMZfd7ZISHdQ"))
    test_location = (45, -94.23456)

    test_places = ["bar", "restaurant"]

    test_radius = 1000000

    test = call_get_cached(test_location, test_places, test_radius)
    pass


