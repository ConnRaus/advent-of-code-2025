from z3 import IntVector, Optimize, Sum, sat 

with open("input.txt") as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

rawbuttonsets, rawjoltages = [], [] 
for line in lines:
    rawbuttonsets.append([b.strip('()') for b in line[1:-1]])
    rawjoltages.append(line[-1].strip('{}'))

# make list of targets to compare to
targetjoltages = [[int(y) for y in x.split(',')] for x in rawjoltages]

# make lists of buttonsets for each light
# 1s toggle, 0s do nothing
buttonsets = []
for e,s in enumerate(rawbuttonsets):
    buttonset = []
    for b in s:
        button = [0] * len(targetjoltages[e])
        for i in b.split(','):
            button[int(i)] = 1
        buttonset.append(button)
    buttonsets.append(buttonset)

# addition doesnt undo like XOR, too many solutions to brute force
# had to look at other solutions to realize this is a linear equation :(
def find_shortest_presses(targetjoltage, buttons):
    n_buttons = len(buttons)
    n = len(targetjoltage)
    
    X = IntVector('x', n_buttons)
    s = Optimize()

    for x in X:
        s.add(x >= 0)

    # A * X = target
    for i in range(n):
        s.add(Sum(X[k]* buttons[k][i] for k in range(n_buttons)) == targetjoltage[i])
    
    s.minimize(Sum(X))

    if s.check() == sat:
        model = s.model()
        return sum(model.eval(x).as_long() for x in X)  # type: ignore
    
    raise Exception("NO SOLUTION SOMETHING BROKE")

print(sum([find_shortest_presses(targetjoltages[i], buttonsets[i]) for i in range(len(targetjoltages))]))

