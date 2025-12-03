with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def split_every_n_chars(s, n):
    output = []
    for i in range(0, len(s), n):
        output.append(s[i:i+n])
    return output

count = 0
ranges = lines[0].split(',')
for r in ranges:
    startnum, endnum = r.split('-')
    
    for num in range(int(startnum), int(endnum)+1):
        strnum = str(num)
        
        for i in range(1, len(strnum)//2+1):
            splitlist = split_every_n_chars(strnum, i)
            if all(ele == splitlist[0] for ele in splitlist):
                count += num
                break

print(count)

