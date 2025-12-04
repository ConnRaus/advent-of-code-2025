with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total = 0
for line in lines:
    num1 = str(max(int(x) for x in line))
    num1idx = line.find(num1)
    
    # these are atrocious, im just having fun
    candidate1 = str(max((int(x) for x in line[0:num1idx]), default='')) + num1
    candidate2 = num1 + str(max((int(x) for x in line[num1idx+1::]), default='')) 

    total += max(int(candidate1), int(candidate2))

print(total)
