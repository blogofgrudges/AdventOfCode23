import re


limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_game(game):
    meta, data = game.split(':')
    turns = data.split(';')

    meta_pattern = re.compile(r'^Game ([0-9]+)')
    red_pattern = re.compile(r'([0-9]+) red')
    green_pattern = re.compile(r'([0-9]+) green')
    blue_pattern = re.compile(r'([0-9]+) blue')

    game_data = {
        'id': find_score(meta_pattern, meta),
        'scores': [],
        'max_score': {
            'red': 0,
            'green': 0,
            'blue': 0
        }
    }

    for turn in turns:
        turn_data = {
            'red': find_score(red_pattern, turn),
            'green': find_score(green_pattern, turn),
            'blue': find_score(blue_pattern, turn)
        }

        for colour in game_data['max_score'].keys():
            if turn_data[colour] > game_data['max_score'][colour]:
                game_data['max_score'][colour] = turn_data[colour]

        game_data['scores'].append(turn_data)
    return game_data


def find_score(pattern, string):
    results = re.search(pattern, string)
    if results:
        return int(results.groups(0)[0])
    return 0


with open('puzzle_input', 'r') as file:
    valid_games = []
    powers = []
    for line in file:
        game = parse_game(line)

        totals = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        is_valid = True
        for scores in game['scores']:
            for colour in limits.keys():
                if scores[colour] > limits[colour]:
                    is_valid = False

        if is_valid:
            valid_games.append(game['id'])

        power = 1
        for colour in game['max_score'].keys():
            power *= game['max_score'][colour]
        powers.append(power)

    print(f'power total = {sum(powers)}')
