import math
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
    target_distance = race['distance']
    total_time = race['time']

    # t_b^2 - t_b*t_t + d = 0
    # a=1 b=-t_t c=d
    dsc = math.sqrt((total_time ** 2) - (4 * 1 * target_distance))
    r1 = (-total_time + dsc) / 2
    r2 = (-total_time - dsc) / 2

    print(math.floor(r1 - r2))  # imprecise
