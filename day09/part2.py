import itertools

with open("input.txt") as f:
    coords = [tuple(int(x) for x in x.strip().split(',')) for x in f.readlines()]

coords.append(coords[0])

def calc_rect_area(pos1, pos2):
    side1 = abs(pos1[0] - pos2[0]) + 1
    side2 = abs(pos1[1] - pos2[1]) + 1
    return side1 * side2

def is_point_in_rect(point, rect):
    rectX1, rectX2 = sorted([rect[0][0], rect[1][0]])
    rectY1, rectY2 = sorted([rect[0][1], rect[1][1]])
    return rectX1 < point[0] < rectX2 and rectY1 < point[1] < rectY2
        
# make list of all perimeter values
perimeter = []
for i in range(len(coords)-1):
    current = coords[i]
    next = coords[i+1]
    perimeter.append(current)
    # if x values are the same, draw vertical line
    if current[0] == next[0]:
        for i in range(min(current[1], next[1]), max(current[1], next[1])):
            perimeter.append((current[0], i))
    elif current[1] == next[1]: # y's same
        for i in range(min(current[0], next[0]), max(current[0], next[0])):
            perimeter.append((i, current[1]))
    else:
        raise Exception("OH NO")
perimeter = set(perimeter) 

# sort candidate rectangles by descending area
possibleRects = list(itertools.combinations(coords, 2))
possibleRects.sort(key=lambda pair: calc_rect_area(*pair), reverse=True)

maxarea = 0
for rectangle in possibleRects:
    valid = True
    for point in perimeter:
        if is_point_in_rect(point, rectangle): 
            valid = False
            break
    # use first valid rect (biggest in sorted list) 
    if valid: 
        maxarea = max(maxarea, calc_rect_area(*rectangle))
        biggest = rectangle
        break
    
print(maxarea)
