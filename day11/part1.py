from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

graph = defaultdict(tuple)
for line in lines:
    fromNode, toNodes = line[0].replace(':', ''), line[1:]
    graph[fromNode] = tuple(toNodes)
    # ^ typechecker might hate this, its fine

def count_paths(graph, node, target):
    if node == target: return 1
    return sum(count_paths(graph, next, target) for next in graph[node])

print(count_paths(graph, 'you', 'out'))
