import re


max_cards = 0
cards = {}
pattern = re.compile(r'([0-9]+)')
with open('puzzle_input', 'r') as file:
    for index, line in enumerate(file, 1):
        cards[index] = 1
    max_cards = index

    file.seek(0)  # there must be a way to do this in one loop
    for index, line in enumerate(file, 1):
        lhs, rhs_data = line.split('|')
        lhs_data = lhs.split(':')[1]

        winning_numbers = re.findall(pattern, lhs_data)
        all_numbers = re.findall(pattern, rhs_data)
        matching_numbers = list(set(winning_numbers) & set(all_numbers))  # very fancy

        for m in range(1, len(matching_numbers) + 1):
            if (index + m) > max_cards:  # out of bounds
                continue
            cards[index + m] += cards[index]  # since all cards are same add the number of cards

    total = sum(cards.values())
    print(total)
