import re


races = []
with open('puzzle_input', 'r') as file:
    for index, line in enumerate(file):
        lhs, data = line.split(':')
        values = re.findall(r'([0-9]+)', data)

        for i, v in enumerate(values):
            if index == 0:
                r = {
                    'time': int(v),
                    'distance': 0
                }
                races.append(r)
            else:
                races[i]['distance'] = int(v)

all_ways_to_win = []
for race in races:
    acceleration = 1
    target_distance = race['distance']
    total_time = race['time']
    ways_to_win = 0
    for this_second in range(0, total_time + 1):
        speed = acceleration * this_second
        remaining_time = total_time - this_second
        possible_distance = speed * remaining_time
        if possible_distance > target_distance:
            ways_to_win += 1
    all_ways_to_win.append(ways_to_win)

total_ways_to_win = 1
for w in all_ways_to_win:
    total_ways_to_win *= w
print(total_ways_to_win)