class Location:
    name = ""
    lat = 0.0
    lng = 0.0

    def __init__(self, str_name):
        self.name = str_name

    def set_lat(self, latitude):
        self.lat = latitude

    def set_lng(self, longitude):
        self.lng = longitude