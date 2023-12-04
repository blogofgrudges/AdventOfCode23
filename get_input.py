import argparse

import requests


"""
like:
get_input.py 4 ../aoc_session
"""

a_parser = argparse.ArgumentParser()
a_parser.add_argument('day', type=int)
a_parser.add_argument('session', type=str)
args = a_parser.parse_args()

with open(args.session, 'r') as session_file:
    session = session_file.read()

url = f'https://adventofcode.com/2023/day/{args.day}/input'
content = requests.get(url, cookies={'session': session})

with open('puzzle_input', 'w') as file:
    file.write(content.text)
