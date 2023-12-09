import re

histories = []
pattern = re.compile(r'([-0-9]+)')
with open('puzzle_input', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        history = []
        for m in matches:
            history.append(int(m))
        histories.append(history)

next_values = []
for history in histories:
    values = history.copy()
    differences = []
    while any(values) != 0:
        difference = []
        for index, value in enumerate(values):
            if index + 1 >= len(values):
                continue
            diff = values[index + 1] - value
            difference.append(diff)
        values = difference
        differences.append(difference)

    for index, difference in reversed(list(enumerate(differences))):
        if difference == differences[-1]:
            difference.append(0)
        else:
            difference.append(difference[-1] + differences[index + 1][-1])
    next_values.append(history[-1] + differences[0][-1])
print(sum(next_values))
