import re


with open('puzzle_input', 'r') as file:
    all_numbers = {}
    all_chars = {}

    symbols_pattern = re.compile(r'[^\w\d\s:.]')
    for i, line in enumerate(file):
        numbers_pattern = re.compile(r'([0-9]+)')

        numbers_matches = re.finditer(numbers_pattern, line)
        all_numbers[i] = []
        for nm in numbers_matches:
            lower = nm.span()[0] - 1
            if lower < 0:
                lower = 0

            upper = nm.span()[1] + 1
            if upper > len(line):
                upper = len(line)

            pos = (lower, upper)
            all_numbers[i].append({'is_valid': False, 'value': int(nm.group()), 'pos': pos})

        all_chars[i] = line.rstrip()

    # loop through the lines in numbers
    total_valid = 0
    for line, numbers in all_numbers.items():
        is_valid = False

        # check the line above
        line_above = line - 1
        line_below = line + 1

        for number in numbers:
            if number['is_valid'] is False:
                # line above
                if line_above >= 0:
                    for index, character in enumerate(all_chars[line_above]):
                        if re.match(symbols_pattern, character):
                            if index in range(*number['pos']):
                                number['is_valid'] = True
                                total_valid += number['value']

                # same line
                for index, character in enumerate(all_chars[line]):
                    if re.match(symbols_pattern, character):
                        if index in range(*number['pos']):
                            number['is_valid'] = True
                            total_valid += number['value']

                # line below
                if line_below <= i:
                    for index, character in enumerate(all_chars[line_below]):
                        if re.match(symbols_pattern, character):
                            if index in range(*number['pos']):
                                number['is_valid'] = True
                                total_valid += number['value']
    print(total_valid)
