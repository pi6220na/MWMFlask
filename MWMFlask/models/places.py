from time import time
import datetime


class Place(object):
    def __init__(self, place_name: str, place_id: str=None, location=None, address: str=None, place_types: [str]=None,
                 created: time()=None):
        self.name = place_name
        self.types = place_types
        self.address = address
        self.place_id = place_id
        if created is not None:
            if isinstance(created, float):
                self.created = created
            else:
                self.created = time()
        else:
            self.created = time()

        # still in progress
        if location is not None:
            if isinstance(location, tuple):
                self.latitude = location[0]
                self.longitude = location[1]
            if isinstance(location, dict):
                self.latitude = location["lat"]
                self.longitude = location["lng"]

    def __str__(self) -> str:
        return "need to implement __str__"

    def __repr__(self) -> str:
        return "<Place object at {}>".format(hex(id(self)))

    def refresh_needed(self, obj):
        pass
        # if self.

    def get_database_args(self) -> tuple:
        return self.name, self.place_id, self.types, self.latitude, self.longitude, self.address


class Dining(Place):
    def __init__(self, dining_name, place_id: str=None, location=None, address: str=None, place_types="dining",
                 created=None):
        super().__init__(dining_name, place_id, location, address, created=created)
        self.type = place_types


class Restaurant(Dining):
    def __init__(self, restaurant_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(dining_name=restaurant_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "restaurant"


class Cafe(Dining):
    def __init__(self, cafe_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(dining_name=cafe_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "cafe"


class Takeout(Dining):
    def __init__(self, meal_takeaway_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(dining_name=meal_takeaway_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "meal_takeaway"


class Bakery(Dining):
    def __init__(self, bakery_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(dining_name=bakery_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "bakery"


class Nightlife(Place):
    def __init__(self, nightlife_name, place_id: str=None, location=None, address: str=None, place_types="nightlife",
                 created=None):
        super().__init__(nightlife_name, place_id, location=location, address=address,
                         created=created)
        self.type = place_types


class Nightclub(Nightlife):
    def __init__(self, night_club_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(nightlife_name=night_club_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "night_club"


class Bar(Nightlife):
    def __init__(self, bar_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(nightlife_name=bar_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "bar"


class Art(Place):
    def __init__(self, art_name, place_id: str=None, location=None, address: str=None, place_types="art",
                 created=None):
        super().__init__(art_name, place_id, location, address, created=created)
        self.type = place_types


class Gallery(Art):
    def __init__(self, gallery_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(art_name=gallery_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "art_gallery"


class Museum(Art):
    def __init__(self, museum_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(art_name=museum_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "museum"


class MovieTheater(Art):
    def __init__(self, theater_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(art_name=theater_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "movie_theater"


class Religious(Place):
    def __init__(self, religious_name, place_id: str=None, location=None, address: str=None, place_types="religious",
                 created=None):
        super().__init__(religious_name, place_id, location, address, created=created)
        self.type = place_types


class Church(Religious):
    def __init__(self, church_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(religious_name=church_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "church"


class Temple(Religious):
    def __init__(self, temple_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(religious_name=temple_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "hindu_temple"


class Mosque(Religious):
    def __init__(self, mosque_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(religious_name=mosque_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "mosque"


class Synagogue(Religious):
    def __init__(self, synagogue_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(religious_name=synagogue_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "synagogue"


class Transport(Place):
    def __init__(self, transport_name, place_id: str=None, location=None, address: str=None,
                 place_types="transportation", created=None):
        super().__init__(transport_name, place_id, location, address, created=created)
        self.type = place_types


class Parking(Transport):
    def __init__(self, parking_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(transport_name=parking_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "parking"


class BusStation(Transport):
    def __init__(self, bus_station_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(transport_name=bus_station_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "bus_station"


class SubwayStation(Transport):
    def __init__(self, subway_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(transport_name=subway_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "subway_station"


class Athletic(Place):
    def __init__(self, athletic_name, place_id: str=None, location=None, address: str=None, place_types="athletic",
                 created=None):
        super().__init__(athletic_name, place_id, location, address, created=created)
        self.type = place_types


class BowlingAlley(Athletic):
    def __init__(self, bowling_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(athletic_name=bowling_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "bowling_alley"


class Stadium(Athletic):
    def __init__(self, stadium_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(athletic_name=stadium_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "stadium"


class Outdoor(Place):
    def __init__(self, outdoor_name, place_id: str=None, location=None, address: str=None, place_types="park",
                 created=None):
        super().__init__(outdoor_name, place_id, location, address, created=created)
        self.type = place_types


class AmusementPark(Outdoor):
    def __init__(self, amusement_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(outdoor_name=amusement_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "amusement_park"


class Aquarium(Outdoor):
    def __init__(self, aquarium_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(outdoor_name=aquarium_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "aquarium"


class Zoo(Outdoor):
    def __init__(self, zoo_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(outdoor_name=zoo_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "zoo"


class Park(Outdoor):
    def __init__(self, park_name, place_id: str=None, location=None, address: str=None, created: time()=time()):
        super().__init__(outdoor_name=park_name, place_id=place_id, location=location, address=address,
                         created=created)
        self.type = "park"


places = [Church("Churches"),
          Temple("Hindu Temple"),
          Mosque("Mosques"),
          Synagogue("Synagogue"),

          AmusementPark("Amusement Parks"),
          Aquarium("Aquariums"),
          Park("Parks"),
          Zoo("Zoos"),

          Nightclub("Night Clubs"),
          Bar("Bars"),

          Gallery("Art Galleries"),
          MovieTheater("Movie Theaters"),
          Museum("Museums"),

          Bakery("Bakeries"),
          Restaurant("Restaurant"),
          Cafe("Cafes"),
          Takeout("Takeout Restaurants"),

          BowlingAlley("Bowling Alleys"),
          Stadium("Stadiums"),

          Parking("Parking"),
          BusStation("Bus Stations"),
          SubwayStation("Subway Stations")
          ]

place_classes = {"church": Church,
                 "hindu_temple": Temple,
                 "mosque": Mosque,
                 "synagogue": Synagogue,

                 "amusement_park": AmusementPark,
                 "aquarium": Aquarium,
                 "park": Park,
                 "zoo": Zoo,

                 "night_club": Nightclub,
                 "bar": Bar,

                 "art_gallery": Gallery,
                 "movie_theater": MovieTheater,
                 "museum": Museum,

                 "bakery": Bakery,
                 "restaurant": Restaurant,
                 "cafe": Cafe,
                 "meal_takeaway": Takeout,

                 "bowling_alley": BowlingAlley,
                 "stadium": Stadium,

                 "parking": Parking,
                 "bus_station": BusStation,
                 "subway_station": SubwayStation
                 }


if __name__ == '__main__':

    ts = time()

    print(ts)

    print(type(ts))

    t = Place("test", (234, 657))
    print(t.types)
    print(t.name)
    print(t.longitude)
    print(t.latitude)

    r = Restaurant("chim", (456, 890))
    print(r.type)
    print(r.name)
    print(r.longitude)
    print(r.latitude)

    print(r)

    crd = {'lat': 45.0201769, 'lng': -93.23676499999999}

    p = Park("audo", crd)

    print(p.type)
    print(p.name)
    print(p.longitude)
    print(p.latitude)

    print()
    print(time())

    for i in p.__dict__:
        print(i)



