import re


def find_in_range(value, map_to_search):
    mapped_value = value
    for rang in map_to_search['ranges']:
        if value in range(rang['source_start'], rang['source_start'] + rang['range']):
            offset = value - rang['source_start']
            mapped_value = rang['destination_start'] + offset
    return mapped_value


seeds_to_plant = []
maps = {}
with open('puzzle_input', 'r') as file:
    for line in file:
        if line.startswith('seeds:'):
            matches = re.findall(r'([0-9]+)', line)
            for m in matches:
                seeds_to_plant.append(int(m))
            continue

        if line[0].isalpha():
            current_map_name = re.search(r'([a-z\-]+)', line).groups()[0]
            maps[current_map_name] = {'ranges': []}
        else:
            results = re.search(r'([0-9]+) ([0-9]+) ([0-9]+)', line)
            if results:
                r = {
                    'destination_start': int(results.groups()[0]),
                    'source_start': int(results.groups()[1]),
                    'range': int(results.groups()[2])
                }
                maps[current_map_name]['ranges'].append(r)

locations = []
for seed in seeds_to_plant:
    value = seed
    for m in maps.keys():
        new_value = find_in_range(value, maps[m])
        value = new_value
        if m == 'humidity-to-location':
            locations.append(new_value)

locations.sort()
print(locations[0])

