with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def find_largest_n_digit_number(num):
    
    if len(str(num)) <= 12:
        return num
    
    for i in range(len(str(num))-1):
        if str(num)[i] < str(num)[i+1]:
            # remove first number
            removednum = str(num)[0:i] + str(num)[i+1::]
            return find_largest_n_digit_number(removednum)

    # else find smallest number in whole string, remove last instance of it
    removeidx = str(num).rfind(min(str(num)))
    removednum = str(num)[0:removeidx] + str(num)[removeidx+1::]

    return find_largest_n_digit_number(removednum)

total = 0
for line in lines:
    # print(find_largest_n_digit_number(line))
    total += int(find_largest_n_digit_number(line))
print(total)
