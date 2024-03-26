import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

combinations = dict()

for m in range(1, 1000):
    for n in range(1, m):
        if is_coprime(m, n) and (m%2 == 0 or n%2 == 0) and not (m%2 == 0 and n%2 == 0):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if (a+b+c) <= 1_500_000:
                if (a+b+c) in combinations:
                    combinations[a+b+c] += 1
                else:
                    combinations[a+b+c] = 1
            k = 2
            while True:
                if k*(a+b+c) <= 1_500_000:
                    if (k*(a+b+c)) in combinations:
                        combinations[k*(a+b+c)] += 1
                    else:
                        combinations[k*(a+b+c)] = 1
                    k += 1
                else:
                    break

count = sum(1 for value in combinations.values() if value == 1)
print(count)