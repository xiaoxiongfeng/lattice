total = 0

def get_mul(num):
    sum = 1
    while num > 1:
        sum *= num
        num -= 1
    return sum
def get_num(s, num, d, sum):
    if d <= 0:
        return
    if sum <= 0:
        return
    if num * num > sum:
        get_num(s, num - 1, d, sum)
    if num * num == sum:
        global total
        total += 2**(27-d+1) * get_mul(len(set(s+str(num))))
        # print(24-d+1, len(set(s+str(num))) - 1)
        print(s + str(num) + '0' * (d - 1) + '   ' + str(2**(24-d+1) * get_mul(len(set(s+str(num))) - 1)))
    while num > 0:
        if num * num < sum:
            # print(s + str(num), num - 1, d - 1, sum - num * num)
            if (num)**2 <=  sum - num * num:
                get_num(s + str(num), num, d - 1, sum - num * num)
            else:
                get_num(s + str(num), num - 1, d - 1, sum - num * num)
        num -= 1
get_num(' ', 8, 24, 79)
print(total)