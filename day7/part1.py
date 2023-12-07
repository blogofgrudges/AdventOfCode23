cards_scores = list('23456789TJQKA')
winning_hands = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
hands = []
with open('puzzle_input', 'r') as file:
    for line in file:
        cards_in_hand, bid = line.split(' ')
        hand = {
            'hand': cards_in_hand,
            'result': 0,
            'bid': int(bid),
            'cards': {}
        }
        for card_in_hand in cards_in_hand:
            if card_in_hand in hand['cards'].keys():
                hand['cards'][card_in_hand] += 1
            else:
                hand['cards'][card_in_hand] = 1

        sorted_cards_in_hand = sorted(list(hand['cards'].values()), reverse=True)
        hand['result'] = winning_hands.index(sorted_cards_in_hand)
        hands.append(hand)

ol = sorted(hands, key=lambda h: (h['result'],
                                  cards_scores.index(h['hand'][0]),
                                  cards_scores.index(h['hand'][1]),
                                  cards_scores.index(h['hand'][2]),
                                  cards_scores.index(h['hand'][3]),
                                  cards_scores.index(h['hand'][4])))

total_winnings = 0
for index, hand in enumerate(ol, 1):
    total_winnings += (hand['bid'] * index)
print(total_winnings)
