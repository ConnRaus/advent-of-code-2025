lines = []
with open("input.txt") as f:
    lines = [x.strip().split() for x in f.readlines()]

# rotate 2d array
equations = []
for i in range(len(lines[0])):
    temp = []
    for j in range(len(lines)):
        ele = lines[j][i]
        temp.append(int(ele) if ele.isdigit() else ele)
    equations.append(temp)

total = 0
for e in equations:
    operator = e[-1]
    match operator:
        case '*':
            # this only works on actual input, for test input remove * e[3]
            # could import math.prod to do it easy like the '+' case
            total += e[0] * e[1] * e[2] * e[3]
        case '+':
            total += sum(e[0:-1])

print(total)
