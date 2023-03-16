from sympy.ntheory import isprime
from math import sqrt

nums = 0
primes = 0
a = 1
b = 0
c = 1
d = 1

while True:
    b += 2
    for _ in range(4):
        a += b
        nums += 1
        if isprime(a):
            primes += 1
        c += a
        d += 1
    if (primes / (1 + nums)) < 0.1:
        print(int(sqrt(a)))
        break