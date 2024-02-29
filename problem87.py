from problem7 import sieveOfEratosthenes
import time
import math

start = time.time()
CEILING = 50_000_000
primes = sieveOfEratosthenes(int(math.sqrt(CEILING) + 1))[:-1]

numbers = set()

squares = [x**2 for x in primes if x**2 < CEILING]
cubes = [x**3 for x in primes if x**3 < CEILING]
fourths = [x**4 for x in primes if x**4 < CEILING]

for i in squares:
    for j in cubes:
        if i + j >= CEILING:
            break
        for k in fourths:
            if i + j + k >= CEILING:
                break
            numbers.add(i+j+k)

print(len(numbers))
print(time.time() - start)