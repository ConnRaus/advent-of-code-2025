ranges = []
with open("input.txt") as f:
    for line in f.readlines():
        if '-' in line: 
            a,b = line.strip().split('-')
            ranges.append([int(a), int(b)])
            
ranges.sort()

mergedRanges = []
start, end = ranges[0]
for ele in ranges:
    if ele[0] > end:
        mergedRanges.append([start, end])
        start = ele[0]
    if ele[1] > end:
        end = ele[1]
mergedRanges.append([start, end])

count = sum([ele[1]-ele[0]+1 for ele in mergedRanges]) 
print(count)
