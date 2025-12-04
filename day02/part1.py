with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

count = 0
ranges = lines[0].split(',')
for r in ranges:
    startnum, endnum = r.split('-')

    for num in range(int(startnum), int(endnum)+1):
        firsthalf = str(num)[0:len(str(num))//2]
        secondhalf = str(num)[len(str(num))//2::]

        if firsthalf == secondhalf:
            count += num

print(count)
