import requests
import json
import time

# read and apply config
config_file = "config.json"
filename = ""
location_file = ""
api_key = ""
start = 0
end = 0

with open(config_file, "r") as f:
    config = json.load(f)
    filename = config['geocoding_target_file']
    location_file = config['location_entity_file']
    start = config['start']
    end = config['end']
    api_key = config['api_key']

arr_location_name = None
with open(location_file, "r") as f:
    arr_location_name = json.load(f)

counter = 1
print(arr_location_name)

# request API
for location_name in arr_location_name:
    if counter in range(start,end+1):
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location_name + "&key=" + api_key
        response = requests.get(url)
        obj_coordinate = {}
        print(response.json())
        results = response.json()['results']

        # parse result
        if results is not None and len(results) > 0:
            location_coordinate = response.json()['results'][0]['geometry']['location']
            lat = location_coordinate['lat']
            lng = location_coordinate['lng']
            obj_coordinate = {'lat': location_coordinate['lat'],
                              'lng': location_coordinate['lng']}

        obj_location = {location_name: obj_coordinate}
        print(counter, json.dumps(obj_location))

        # write into jsonl
        with open(filename, 'a') as jsonl:
            jsonl.write(json.dumps(obj_location) + "\n")

        time.sleep(0.02)

    counter += 1