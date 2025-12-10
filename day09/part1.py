import itertools

with open("input.txt") as f:
    coords = [tuple(int(x) for x in x.strip().split(',')) for x in f.readlines()]

def calc_rect_area(pos1, pos2):
    side1 = abs(pos1[0] - pos2[0]) + 1
    side2 = abs(pos1[1] - pos2[1]) + 1
    return side1 * side2

# this is probably the slowest way to do this, 
# but runs fast enough for part 1
max = 0
bestpair = None
for i in itertools.combinations(coords, 2):
    area = calc_rect_area(i[0], i[1])
    if area > max:
        bestpair = i
        max = area 

print(max)
