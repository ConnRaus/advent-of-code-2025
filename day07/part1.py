with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

carrots = set()
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c == '^': carrots.add((j, i))

# path starts at 'S'
path = set()
path.add((lines[0].index('S'), 0))

splits = 0
for i in range(len(lines)-1):
    pathLayer = [x for x in path if x[1] == i]
    
    for point in pathLayer:
        if (point[0], point[1] + 1) in carrots:
            path.add((point[0] - 1, point[1] + 1))
            path.add((point[0] + 1, point[1] + 1))
            splits += 1
        else:
            path.add((point[0], point[1] + 1))

print(splits)

