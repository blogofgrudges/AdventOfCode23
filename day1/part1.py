import re


def calibration_values(values):
    if len(values) >= 2:
        return int(values[0] + values[-1])
    else:
        return int(values[0] * 2)


pattern = re.compile(r'([0-9])')

total = 0
with open('puzzle_input') as file:
    for line in file:
        matches = re.findall(pattern, line)
        print(matches)
        total += calibration_values(matches)

print(total)
