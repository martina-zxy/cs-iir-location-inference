import requests
from entity import Location
import csv
import os.path
import json

# read and apply config
config_file = "config.json"
json_data=open(config_file).read()
config = json.loads(json_data)
filename = config['geocoding_target_file']

arr_location_name = ["Lyon,France"]

# request API
for i in range(0,len(arr_location_name)):
    location_name = arr_location_name[i] # I want to keep track of the index
    loc = Location(location_name)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location_name + "&key=AIzaSyCdVEEVmkDRdyKxSHBrnLdD66GPI0BCFts"
    response = requests.get(url)
    results = response.json()['results']

    if results is not None and len(results) > 0:
        location_coordinate = response.json()['results'][0]['geometry']['location']

        loc.set_lat(location_coordinate['lat'])
        loc.set_lng(location_coordinate['lng'])
        print(i, loc.name, loc.lat, loc.lng)

        # make title if file does not exist
        if not os.path.isfile(filename):
            with open(filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
                writer.writerow(["location_name", "latitude", "longitude"])

        # write into csv
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
            writer.writerow([loc.name, loc.lat, loc.lng])


