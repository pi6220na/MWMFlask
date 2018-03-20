from time import time
from datetime import datetime
import datetime
import json


class Place(object):
    def __init__(self, place_name: str=None, place_id: str=None, location=None, address: str=None,
                 place_types: [str]=None, created: datetime=None):
        self.name = place_name
        self.types = place_types
        self.address = address
        self.place_id = place_id
        if created is not None:
            if isinstance(created, datetime.datetime):
                self.created = created
            else:
                self.created = datetime.datetime.now()
        else:
            self.created = datetime.datetime.now()

        # still in progress
        if location is not None:
            if isinstance(location, tuple):
                self.latitude = round(location[0], 7)
                self.longitude = round(location[1], 7)
            if isinstance(location, dict):
                self.latitude = round(location["lat"], 7)
                self.longitude = round(location["lng"], 7)

    def __str__(self) -> str:
        return json.dumps(self.to_json())
        # return "need to implement __str__"

    def __repr__(self) -> str:
        return "<Place object at {}>".format(hex(id(self)))

    def __eq__(self, other) -> bool:
        return self.place_id == other.place_id

    def __hash__(self) -> int:
        return hash(('place_id', self.place_id))

    def cache_expired(self):
        if datetime.datetime.now() - self.created > datetime.timedelta(hours=1):
            return True
        else:
            return False

    def to_json(self):
        return {'name': self.name, 'place_id': self.place_id, 'address': self.address,
                'location': {'lat': self.latitude, 'lng': self.longitude},
                'place_types': self.types, 'created': str(self.created).split(".")[0]}

    def update_cache(self):
        pass

    def get_database_args(self) -> tuple:
        return self.name, self.place_id, self.latitude, self.longitude, self.address


places = [Place("Churches", place_types=["church"]),
          Place("Hindu Temple", place_types=["hindu_temple"]),
          Place("Mosques", place_types=["mosque"]),
          Place("Synagogue", place_types=["synagogue"]),

          Place("Amusement Parks", place_types=["amusement_park"]),
          Place("Aquariums", place_types=["aquarium"]),
          Place("Parks", place_types=["park"]),
          Place("Zoos", place_types=["zoo"]),

          Place("Night Clubs", place_types=["night_club"]),
          Place("Bars", place_types=["bar"]),

          Place("Art Galleries", place_types=["art_gallery"]),
          Place("Movie Theaters", place_types=["movie_theater"]),
          Place("Museums", place_types=["museum"]),

          Place("Bakeries", place_types=["bakery"]),
          Place("Restaurant", place_types=["restaurant"]),
          Place("Cafes", place_types=["cafe"]),
          Place("Takeout Restaurants", place_types=["meal_takeaway"]),

          Place("Bowling Alleys", place_types=["bowling_alley"]),
          Place("Stadiums", place_types=["stadium"]),

          Place("Parking", place_types=["parking"]),
          Place("Bus Stations", place_types=["bus_station"]),
          Place("Subway Stations", place_types=["subway_station"])
          ]


type_strings = ["church",
                "hindu_temple",
                "mosque",
                "synagogue",

                "amusement_park",
                "aquarium",
                "park",
                "zoo",

                "night_club",
                "bar",

                "art_gallery",
                "movie_theater",
                "museum",

                "bakery",
                "restaurant",
                "cafe",
                "meal_takeaway",

                "bowling_alley",
                "stadium",

                "parking",
                "bus_station",
                "subway_station"]


if __name__ == '__main__':

    one_hour_and_a_half_ago = datetime.datetime.now() - datetime.timedelta(hours=1, minutes=30)
    now = datetime.datetime.now()
    half_hour_ago = datetime.datetime.now() - datetime.timedelta(minutes=30)

    # print(type(one_hour_and_a_half_ago))

    place_one = Place("Place One: ", created=one_hour_and_a_half_ago)
    place_two = Place("Place Two: ", created=half_hour_ago)

    print(place_one.name)
    print(place_one.cache_expired())

    if place_one.cache_expired():
        print(place_one.name)
        print("expired")

    if place_two.cache_expired():
        print(place_two.name)
        print("not expired")


