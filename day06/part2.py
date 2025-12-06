from math import prod

lines = []
with open("input.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]

# read char by char on all lines simultaneously
idx = 0
strings = []
while idx < len(lines[0]):
    temp = ''
    for row in range(len(lines)):
        temp += lines[row][idx]
    strings.append(temp)
    idx += 1

# split equations into separate arrays
chunks = []
temp = []
for s in strings:
    if len(s.strip()) > 0:
        temp.append(s.strip())
    else:
        chunks.append(temp)
        temp = []
chunks.append(temp)

# get + or * out of first number
for e in chunks:
    if '+' in e[0]:
        e.append('+')
        e[0] = e[0].replace('+', '').strip()
    elif '*' in e[0]:
        e.append('*')
        e[0] = e[0].replace('*', '').strip()

# make strings numbers
for e in chunks:
    for i in range(len(e[0:-1])):
        e[i] = int(e[i])

# calculate things
total = 0
for equation in chunks:
    match equation[-1]:
        case '+':
            total += sum(equation[0:-1])
        case '*':
            total += prod(equation[0:-1])

print(total)
