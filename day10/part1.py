import itertools

with open("input.txt") as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

rawlights, rawbuttonsets = [], [] 
for line in lines:
    rawlights.append(line[0].strip('[]'))
    rawbuttonsets.append([b.strip('()') for b in line[1:-1]])

# make list of targets to compare to
targetlights = []
for light in rawlights:
    temp = [0] * len(light)
    for i in range(len(light)):
        if light[i] == '#': temp[i] = 1
    targetlights.append(temp)
#print(targetlights)

# make lists of buttonsets for each light
# 1s toggle, 0s do nothing
buttonsets = []
for e,s in enumerate(rawbuttonsets):
    buttonset = []
    for b in s:
        button = [0] * len(targetlights[e])
        for i in b.split(','):
            button[int(i)] = 1
        buttonset.append(button)
    buttonsets.append(buttonset)
#print(buttonsets)

# XORing the same thing twice just undoes it
# so never have to press each button more than once
def find_shortest_presses(targetlight, buttons):
    for i in range(len(buttons)):
        buttoncombos = itertools.combinations(buttons, i)
        for presses in buttoncombos:
            templight = [0] * len(targetlight)
            for press in presses:
                templight = [a ^ b for a,b in zip(templight, press)]
            if templight == targetlight:
                return i
    raise Exception("NOT FOUND, CODE BROKE")

print(sum([find_shortest_presses(targetlights[i], buttonsets[i]) for i in range(len(targetlights))]))


