import re


with open('puzzle_input', 'r') as file:
    all_symbols = {}
    all_numbers = {}
    all_chars = {}

    symbols_pattern = re.compile(r'[*]')
    numbers_pattern = re.compile(r'([0-9]+)')
    for i, line in enumerate(file):
        symbols_matches = re.finditer(symbols_pattern, line)
        all_symbols[i] = []
        for sm in symbols_matches:
            lower = sm.span()[0] - 1
            if lower < 0:
                lower = 0

            upper = sm.span()[1] + 1
            if upper > len(line):
                upper = len(line)

            pos = (lower, upper)
            all_symbols[i].append({'pos': pos, 'adj_numbers': []})

        numbers_matches = re.finditer(numbers_pattern, line)
        all_numbers[i] = []
        for nm in numbers_matches:
            lower = nm.span()[0]
            upper = nm.span()[1]

            pos = (lower, upper)
            all_numbers[i].append({'value': int(nm.group()), 'pos': pos})

    # loop through the lines in symbols
    total_valid = 0
    for line, symbols in all_symbols.items():
        is_valid = False

        # check the line above
        line_above = line - 1
        line_below = line + 1

        for symbol in symbols:
            if line_above >= 0:
                for number in all_numbers[line_above]:
                    for j in range(*symbol['pos']):
                        if j in range(*number['pos']):
                            if number['value'] not in symbol['adj_numbers']:
                                symbol['adj_numbers'].append(number['value'])

            # same line
            for number in all_numbers[line]:
                for j in range(*symbol['pos']):
                    if j in range(*number['pos']):
                        if number['value'] not in symbol['adj_numbers']:
                            symbol['adj_numbers'].append(number['value'])

            if line_below <= i:
                for number in all_numbers[line_below]:
                    for j in range(*symbol['pos']):
                        if j in range(*number['pos']):
                            if number['value'] not in symbol['adj_numbers']:
                                symbol['adj_numbers'].append(number['value'])

    gear_ratios = []
    for line, symbols in all_symbols.items():
        for symbol in symbols:
            if len(symbol['adj_numbers']) == 2:
                gear_ratios.append(symbol['adj_numbers'][0] * symbol['adj_numbers'][1])
    print(sum(gear_ratios))
