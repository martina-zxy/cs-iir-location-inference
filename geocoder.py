import requests
from entity import Location
import csv
import os.path

filename = "location1.csv"
arr_location_name = ["Lyon,France", "Paris,France"]

for location_name in arr_location_name:
    loc = Location(location_name)
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + location_name

    response = requests.get(url)
    location_coordinate = response.json()['results'][0]['geometry']['location']

    loc.set_lat(location_coordinate['lat'])
    loc.set_lng(location_coordinate['lng'])
    print(loc.name, loc.lat, loc.lng)

    if not os.path.isfile(filename):
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
            writer.writerow(["location_name", "latitude", "longitude"])

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        writer.writerow([loc.name, loc.lat, loc.lng])


