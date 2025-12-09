from collections import defaultdict
from functools import lru_cache 

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

carrots = set()
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c == '^': carrots.add((j, i))

# paths starts at 'S'
paths = defaultdict(list)
start = (lines[0].index('S'), 0)
paths[start] = []

# create actual tree with all connections
for i in range(len(lines)-1):
    
    pathsLayer = [x for x in list(paths.keys()) if x[1] == i]

    for point in pathsLayer:

        if (point[0], point[1] + 1) in carrots:
            downleft = (point[0] - 1, point[1] + 1)
            downright = (point[0] + 1, point[1] + 1)
            paths[point].append(downleft)
            paths[point].append(downright)
            paths[downleft] = []
            paths[downright] = []
        else:
            downstraight = (point[0], point[1] + 1)
            paths[point].append(downstraight)
            paths[downstraight] = []

@lru_cache
def countpaths(node):
    children = paths[node]
    if not children: # leaf
        return 1
    return sum(countpaths(child) for child in children)
  
print(countpaths(start))
