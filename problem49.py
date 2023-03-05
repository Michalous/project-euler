import itertools
from problem7 import sieveOfEratosthenes

x = sieveOfEratosthenes(10000)
y = sieveOfEratosthenes(1000)
primes = list(set(x) - set(y))
primes.sort()

for prime in primes:
    prime_permutations = []
    for p in itertools.permutations(str(prime)):
        perm = int(''.join(str(x) for x in p))
        if perm in primes and perm not in prime_permutations:
            prime_permutations.append(perm)
            primes.remove(perm)
    if len(prime_permutations) > 2:
        prime_permutations.sort()
        for i in prime_permutations:
            for j in prime_permutations:
                diff = i - j
                if diff > 0 and j - diff in prime_permutations:
                    print(prime_permutations)
                    print(j - diff, j, i)
                    print(f'result: {j - diff}{j}{i}')