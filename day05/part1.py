ranges = []
ingredients = []
with open("input.txt") as f:
    for line in f.readlines():
        if '-' in line: 
            a,b = line.strip().split('-')
            ranges.append([int(a), int(b)])
        elif len(line.strip()) != 0: ingredients.append(int(line.strip()))

count = 0
for ingredient in ingredients:
    for ele in ranges:
        if ele[0] <= ingredient <= ele[1]:
            count += 1
            break

print(count)
