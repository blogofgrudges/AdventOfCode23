import re


mapping = {
    'oneight': ['1', '8'],  # there's probably a better way to do these combined words
    'threeight': ['3', '8'],
    'fiveight': ['5', '8'],
    'eightwo': ['8', '2'],
    'eighthree': ['8', '3'],
    'twone': ['2', '1'],
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def decode(value):
    if value in mapping.keys():
        return mapping[value]
    else:
        return value


def calibration_values(values):
    decoded_values = []
    for v in values:
        for decoded_value in decode(v):
            decoded_values.append(decoded_value)

    print(decoded_values)
    if len(decoded_values) >= 2:
        return int(decoded_values[0] + decoded_values[-1])
    else:
        return int(decoded_values[0] * 2)


mapped_keys = '|'.join(mapping.keys())
pattern = re.compile(rf"[0-9]|{'|'.join(mapping.keys())}")

total = 0
with open('puzzle_input') as file:
    for line in file:
        matches = re.findall(pattern, line)
        total += calibration_values(matches)

print(total)
