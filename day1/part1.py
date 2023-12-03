import re


start_pattern = re.compile(r'([0-9]).*$')
end_pattern = re.compile(r'^.*([0-9])')

total = 0
with open('puzzle_input', 'r') as file:
    for line in file:
        first_digit = re.search(start_pattern, line).groups(0)[0]
        last_digit = re.search(end_pattern, line).groups(0)[0]
        total += int(first_digit + last_digit)

print(total)
