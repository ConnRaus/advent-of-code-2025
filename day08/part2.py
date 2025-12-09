import math

with open("input.txt") as f:
    boxes = [x.strip().split(',') for x in f.readlines()]
boxes = [tuple(map(int, row)) for row in boxes]

# calculate all box distances
def make_dist_graph(boxes):
    edges = []
    for i in range(len(boxes)):
        x1, y1, z1 = boxes[i]
        for j in range(i+1, len(boxes)):
            x2, y2, z2 = boxes[j]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            edges.append((distance, i, j,))
    return edges

distanceEdges = sorted(make_dist_graph(boxes))

def getSet(searchBox, connections):
    for s in connections:
        if searchBox in s:
            return s
    raise Exception("couldn't find", searchBox, "in connections")

connections = [{box} for box in boxes] 
i = 0
while True:
    boxPair = distanceEdges[i]
    box1 = boxes[boxPair[1]]
    box2 = boxes[boxPair[2]]

    set1 = getSet(box1, connections) 
    set2 = getSet(box2, connections)
    
    if set1 != set2:
        set1.update(set2)
        connections.remove(set2)

    if len(connections) == 1:
        print(box1[0] * box2[0])
        break
    i+=1
