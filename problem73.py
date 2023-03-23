from math import gcd

res = 0
for d in range(1, 12001):
    for n in range(int(d / 3) + 1, int(d / 2) + 1):
        if gcd(n, d) == 1:
            if (n/d > 1/3 and n/d < 1/2):
                # print(f'{n} / {d}')
                res += 1
print(res)