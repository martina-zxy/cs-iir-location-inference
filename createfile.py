import json

# read and apply config
config_file = "config.json"
filename = ""
location_file = ""
start = 0
end = 0

with open(config_file, "r") as f:
    config = json.load(f)
    filename = config['geocoding_target_file']
    location_file = config['location_entity_file']
    start = config['start']
    end = config['end']

arr_location_name = None
with open(location_file, "r") as f:
    arr_location_name = json.load(f)

counter = 1

print(arr_location_name)
location_map = {}
for loc in arr_location_name:
    if counter in range(7501,10001):
        location_map[loc] = arr_location_name[loc]
        print(counter, loc, arr_location_name[loc])
    counter += 1

print(json.dumps(location_map))
with open('data/location_4.json', 'w') as f:
    json.dump(location_map, f)
#
# print(len(arr_location_name))
