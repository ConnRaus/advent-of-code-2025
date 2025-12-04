with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

count = 0
rotation = 50
for l in lines:
    
    amount = int(l[1:])
    amount = amount%100

    match l[0]:
        case 'R':
            rotation += amount
        case 'L':
            rotation -= amount

    if rotation < 0:
        rotation = rotation + 100
    elif rotation > 99:
        rotation -= 100
    
    if rotation == 0:
        count += 1

print(count)
