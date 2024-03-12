import math

res = 0

def continued_fraction_period(num):
    m, d, a0, a = 0, 1, int(math.sqrt(num)), int(math.sqrt(num))
    period = 0
    if a0 != math.sqrt(num):
        while a != 2 * a0:
            m = d * a - m
            d = (num - m * m) / d
            a = int((a0 + m) / d)
            period += 1
    return period


for i in range(1, 10000):
    if continued_fraction_period(i) % 2 != 0:
        res += 1

print(res)

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm