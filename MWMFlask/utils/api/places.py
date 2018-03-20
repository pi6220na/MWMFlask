from MWMFlask.utils.api import calls
from MWMFlask.models.places import Place
from flask import jsonify
from MWMFlask.utils.database import connection as db


def get_cached(location: tuple, place_types: [str], radius: int):
    print("in places.get_cached: ")

    print("before calls.get_cached_by_radius: ")
    cached = calls.get_cached_by_radius(location=location, search_radius=radius)  #, place_type=place_type)

    print("cached: ")
    print(cached)

    print("before check_for_expired: ")
    expired = check_for_expired(cached)

    print("expired: ")
    print(expired)
    if len(expired) > 0:
        print("before calls.get_places_by_id:")
        refreshed = calls.get_places_by_id(expired)
        print("refreshed: ")
        print(refreshed)
        print("before update_records:")
        update_records(refreshed)

    print("after if")

    pl_list = []

    for t in place_types:
        pl_list.extend([pl for pl in cached if t in pl.types])

    return pl_list


def check_for_expired(cached: [Place]) -> [Place]:
    expired = []
    for record in cached:
        if record.cache_expired():
            expired.append(record)
    return expired


def update_records(refreshed: [Place]) -> None:
    for place in refreshed:
        calls.update_expired_place(place)


def parse_request_types(types: str):
    parsed_types = []
    if '-' in types:
        parsed_types = types.split("-")
    else:
        parsed_types.append(types)
    return parsed_types


def update_cache(location, radius):
    calls.build_cache(location, radius)
    return jsonify({'error': False, 'message': 'Cache has been updated'})


def get_cached_place_by_id(place_id: str) -> Place:
    cached_qry = "SELECT * FROM cache WHERE place_id = ?"
    rs = db.get_rs(cached_qry, (place_id,))

    location = (rs[4], rs[5])
    types = get_types_by_place_id(rs[2])

    return Place(rs[3], rs[2], location, rs[6], types)


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


if __name__ == '__main__':
    print(get_cached_place_by_id("ChIJL_d7hr8ts1IRMZfd7ZISHdQ"))
    pass


