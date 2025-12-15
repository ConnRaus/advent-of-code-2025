with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

# Stupid cheaty way of doing this that worked, just check to 
# see if each shape can get its own 3x3 grid. Tried this after 
# being too dumb to understand algorithm x and it worked.
# "Shapes" are only in an array because my first stupid idea  
# was hard coding how many tiles they took before trying 3x3s.
# Left the code just as ugly as it deserves to be.
shapes = [9, 9, 9, 9, 9, 9]
total = 0
for line in lines:
    if 'x' in line:
        splits = line.split(' ')
        area = int(splits[0][0:2]) * int(splits[0][3:5])
        neededArea = 0
        for i in range(1, len(splits)-1):
             neededArea += int(splits[i]) * shapes[i]
        if area >= neededArea: total += 1

print(total)
