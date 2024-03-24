# slow
import math

res = 0

def sum_of_factorials(num):
    return sum([math.factorial(int(x)) for x in str(num)])

for i in range(1000000):
    list_of_sums = [i]
    while True:
        x = sum_of_factorials(list_of_sums[-1])
        if x not in list_of_sums:
            list_of_sums.append(x)
        else:
            if len(list_of_sums) == 60:
                res += 1
            break
