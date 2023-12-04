import re


with open('puzzle_input', 'r') as file:
    scores = []
    for line in file:
        lhs, rhs_data = line.split('|')
        game, lhs_data = lhs.split(':')
        winning_numbers = re.findall(r'([0-9]+)', lhs_data)
        all_numbers = re.findall(r'([0-9]+)', rhs_data)

        score = 0
        for winning_number in winning_numbers:
            if winning_number in all_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        scores.append(score)

print(sum(scores))
