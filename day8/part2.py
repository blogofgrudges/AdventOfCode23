from functools import reduce
import math
import re


instructions = []
nodes = {}
pattern = re.compile(r'([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)')
with open('puzzle_input', 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            instructions = list(line.rstrip())
        else:
            matches = re.search(pattern, line)
            if matches:
                nodes[matches.groups()[0]] = {'L': matches.groups()[1], 'R': matches.groups()[2]}

start_nodes = []
end_nodes = []
for node in nodes.keys():
    if node.endswith('A'):
        start_nodes.append(node)
    if node.endswith('Z'):
        end_nodes.append(node)

nodes_steps = []
for node in start_nodes:
    steps = 0
    i = 0
    while node.endswith('Z') is False:
        directions = nodes[node]
        node = directions[instructions[i]]
        steps += 1
        i += 1
        if i >= len(instructions):
            i = 0
    nodes_steps.append(steps)

product = 1
for i in nodes_steps:
    product *= i

print(nodes_steps)
print(reduce((lambda x, y: int(x*y / math.gcd(x, y))), nodes_steps))
