import re


instructions = []
nodes = {}
pattern = re.compile(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)')
with open('puzzle_input', 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            instructions = list(line.rstrip())
        else:
            matches = re.search(pattern, line)
            if matches:
                nodes[matches.groups()[0]] = {'L': matches.groups()[1], 'R': matches.groups()[2]}

start_node = nodes['AAA']
end_node = nodes['ZZZ']
steps = 0
i = 0
current_node = start_node
while current_node != end_node:
    current_node = nodes[current_node[instructions[i]]]
    i += 1
    if i >= len(instructions):
        i = 0
    steps += 1

print(steps)
