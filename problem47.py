from problem7 import sieveOfEratosthenes
from math import sqrt

primes = sieveOfEratosthenes(400)

def primeFactors(n):
    # Takes in a positive integer and returns an array of its prime factors.
    array = []
    for prime in primes:
        x = 0
        if prime > (sqrt(n) + 1):
            break
        while n % prime == 0:
            x += 1
            n /= prime
            if x == 1:
                array.append(prime)
            else:
                array[-1] *= prime
    if n != 1:
        array.append(int(n))
    return array

for i in range(30, 150000):
    if len(primeFactors(i)) == 4:
        w = set(primeFactors(i))
        if len(primeFactors(i + 1)) == 4:
            x = set(primeFactors(i + 1))
            if len(primeFactors(i + 2)) == 4:
                y = set(primeFactors(i + 2))
                if len(primeFactors(i + 3)) == 4:
                    z = set(primeFactors(i + 3))
                    primeFacts = w.union(x).union(y).union(z)
                    if len(primeFacts) == 16:
                        print(i)
                        break