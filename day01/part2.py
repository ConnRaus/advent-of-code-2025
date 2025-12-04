with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

count = 0
rotation = 50
for l in lines:
    
    amount = int(l[1:])
    count += amount//100
    amount = amount%100

    # kind of ugly, not proud of this part
    if rotation == 0 and l[0] == 'L':
        rotation -= amount
        rotation += 100
        continue


    match l[0]:
        case 'R':
            rotation += amount
        case 'L':
            rotation -= amount

    if rotation < 0:
        count += 1
        rotation = rotation + 100
    elif rotation == 0:
        count += 1
    elif rotation > 99:
        count += 1
        rotation -= 100

print(count)
