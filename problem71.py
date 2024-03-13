from fractions import Fraction
num = 3/7 # 3/7 * 1000000 = 428571.4285714285

res = [0, ()]

for n in range(428000, 430000):
    for d in range(999000, 1000000):
        if (n / d < 3/7) and (n / d > res[0]):
            res[0] = n / d
            res[1] = n,d

print(res)
print(Fraction(res[1][0], res[1][1]))