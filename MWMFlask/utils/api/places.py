from MWMFlask.utils.api import calls
from MWMFlask.models.places import Place
from flask import jsonify


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
