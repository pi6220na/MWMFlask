import requests
from MWMFlask.models.places import *
from MWMFlask.Main import app
import MWMFlask.utils.database.connection as db


def query_api(location, radius: int, place_type: str) -> [dict]:
    log_api_params(location, radius, place_type)
    return [{"test": "string"}, {"test": "string"}]


def log_api_params(loc, rad, type):
    pass


def build_request(request_url, api_route, query_string):
    # https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=45.020459,-93.241592&radius=50000&type=bar&key=AIzaSyBnoAOkefgBP2J5_pHYLqrZIbmdLWM1dHc
    # print(url)
    # print(route)
    # print(query)
    return "{}{}{}".format(request_url, api_route, query_string)


def get_places(location, radius):
    queried_places = []
    for t in places:
        qp = places_request(location, radius, t.type)
        for p in qp:
            queried_places.append(p)
    return queried_places


def get_places_by_type(place_type: str) -> [Place]:



    return []


def places_request(location: (float, float), radius: int, place_type: str):

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

        place_obj = place_classes[place_type](place_name, place_id, coordinates, place_address)

        places_of_type.append(place_obj)

    return places_of_type


if __name__ == '__main__':
    latitude = 45.020459
    lng = -93.241592
    rad = 1000
    # p_type = "restaurant"
    # key = "AIzaSyBnoAOkefgBP2J5_pHYLqrZIbmdLWM1dHc"
    #
    # url = "https://maps.googleapis.com/"
    # route = "maps/api/place/nearbysearch/"
    # query = "json?location={},{}&radius={}&type={}&key={}".format(latitude, lng, rad, p_type, key)
    # test = build_request(url, route, query)
    # # print(test)
    #
    # r = requests.get(test)
    #
    # # print(r.status_code)
    # # print(r.json()["results"])
    #
    # results = r.json()["results"]
    #
    # # print(results)
    #
    # for r in results:
    #     # print(r)
    #     print(type(r["geometry"]["location"]))
    #     print(r["geometry"]["location"])
    #     print(r["place_id"])
    #     print(r["name"])
    #     print(r["vicinity"])
    #     print()
    #

    cords = (latitude, lng)
    pl_list = places_request(cords, rad, "restaurant")
    print(pl_list)

    places_from_api = get_places(cords, rad)

    for p in places_from_api:
        print("{}, {}".format(p.name, p.type))

        cache_qry = "INSERT INTO cache (name, place_id, latitude, longitude, address) " \
                    "VALUES (?, ?, ?, ?, ?)"
        db.execute_query(cache_qry, p.get_database_args())

