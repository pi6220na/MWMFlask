class Place(object):
    def __init__(self, place_name, place_type=None):
        self.name = place_name
        self.type = place_type


class Dining(Place):
    def __init__(self, dining_name, place_type="dining"):
        super().__init__(dining_name)
        self.type = place_type


class Restaurant(Dining):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name)
        self.type = "restaurant"


class Cafe(Dining):
    def __init__(self, cafe_name):
        super().__init__(cafe_name)
        self.type = "cafe"


class Takeout(Dining):
    def __init__(self, meal_takeaway_name):
        super().__init__(meal_takeaway_name)
        self.type = "meal_takeaway"


class Bakery(Dining):
    def __init__(self, bakery_name):
        super().__init__(bakery_name)
        self.type = "bakery"


class Nightlife(Place):
    def __init__(self, nightlife_name, place_type="nightlife"):
        super().__init__(nightlife_name)
        self.type = place_type


class Nightclub(Nightlife):
    def __init__(self, night_club_name):
        super().__init__(night_club_name)
        self.type = "night_club"


class Bar(Nightlife):
    def __init__(self, bar_name):
        super().__init__(bar_name)
        self.type = "bar"


class Art(Place):
    def __init__(self, art_name):
        super().__init__(art_name)


class Gallery(Place):
    def __init__(self, gallery_name):
        super().__init__(gallery_name)
        self.type = "art_gallery"


class Museum(Place):
    def __init__(self, museum_name):
        super().__init__(museum_name)
        self.type = "museum"


class MovieTheater(Place):
    def __init__(self, theater_name):
        super().__init__(theater_name)
        self.type = "movie_theater"


class Religious(Place):
    def __init__(self, religious_name, place_type="religious"):
        super().__init__(religious_name)
        self.type = place_type


class Church(Religious):
    def __init__(self, church_name):
        super().__init__(church_name)
        self.type = "church"


class Temple(Religious):
    def __init__(self, temple_name):
        super().__init__(temple_name)
        self.type = "hindu_temple"


class Mosque(Religious):
    def __init__(self, mosque_name):
        super().__init__(mosque_name)
        self.type = "mosque"


class Synagogue(Religious):
    def __init__(self, synagogue_name):
        super().__init__(synagogue_name)
        self.type = "synagogue"


class Transport(Place):
    def __init__(self, transportation_name, place_type="transportation"):
        super().__init__(transportation_name)
        self.type = place_type


class Parking(Transport):
    def __init__(self, parking_name):
        super().__init__(parking_name)
        self.type = "parking"


class BusStation(Transport):
    def __init__(self, bus_station_name):
        super().__init__(bus_station_name)
        self.type = "bus_station"


class SubwayStation(Transport):
    def __init__(self, subway_station_name):
        super().__init__(subway_station_name)
        self.type = "subway_station"


class Athletic(Place):
    def __init__(self, athletic_name, place_type="athletic"):
        super().__init__(athletic_name)
        self.type = place_type


class BowlingAlley(Athletic):
    def __init__(self, bowling_alley_name):
        super().__init__(bowling_alley_name)
        self.type = "bowling_alley"


class Stadium(Athletic):
    def __init__(self, stadium_name):
        super().__init__(stadium_name)
        self.type = "stadium"


class Outdoor(Place):
    def __init__(self, park_name, place_type="park"):
        super().__init__(park_name)
        self.type = place_type


class AmusementPark(Outdoor):
    def __init__(self, amusement_park_name):
        super().__init__(amusement_park_name)
        self.type = "amusement_park"


class Aquarium(Outdoor):
    def __init__(self, aquarium_name):
        super().__init__(aquarium_name)
        self.type = "aquarium"


class Zoo(Outdoor):
    def __init__(self, zoo_name):
        super().__init__(zoo_name)
        self.type = "zoo"


class Park(Outdoor):
    def __init__(self, park_name):
        super().__init__(park_name)
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

