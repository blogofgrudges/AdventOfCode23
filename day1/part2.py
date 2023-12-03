import re


mapping = {
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
    return value


mapped_keys = '|'.join(mapping.keys())

start_pattern = re.compile(rf"([0-9]|{'|'.join(mapping.keys())}).*$")
end_pattern = re.compile(rf"^.*([0-9]|{'|'.join(mapping.keys())})")

total = 0
with open('puzzle_input', 'r') as file:
    for line in file:
        first_digit = re.search(start_pattern, line).groups(0)[0]
        last_digit = re.search(end_pattern, line).groups(0)[0]
        total += int(decode(first_digit) + decode(last_digit))

print(total)
