from problem7 import sieveOfEratosthenes

primes = sieveOfEratosthenes(10000)

doubled_squares = set()

for i in range(1, 100):
    doubled_squares.add(2 * (i**2))

isTrue = True
    
for i in range(9, 10000, 2):
    if not isTrue:
        break
    if i not in primes:
        isTrue = False
        for prime in primes:
            if prime > i:
                break
            x = i - prime
            if x in doubled_squares:
                isTrue = True
                break
        if not isTrue:
            print(i)