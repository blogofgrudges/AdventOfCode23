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
        'scores': []
    }

    for turn in turns:
        turn_data = {
            'red': find_score(red_pattern, turn),
            'green': find_score(green_pattern, turn),
            'blue': find_score(blue_pattern, turn)
        }
        game_data['scores'].append(turn_data)
    return game_data


def find_score(pattern, string):
    results = re.search(pattern, string)
    if results:
        return int(results.groups(0)[0])
    return 0


with open('puzzle_input', 'r') as file:
    valid_games = []
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

    print(f'total = {sum(valid_games)}')
