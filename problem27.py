from problem7 import sieveOfEratosthenes

primes = sieveOfEratosthenes(2000)

a_b_product = 0
longest_run = 0
value_a = 0
value_b = 0

for b in primes[0:168]:
    for a in range(-999, 1001):
        for n in range(0, 1000):
            q = n*n + a*n + b
            if q not in primes:
                if n > longest_run:
                    longest_run = n
                    a_b_product = a * b
                    value_a = a
                    value_b = b
                break

print(f'a = {value_a}, b = {value_b}, product of a and b = {a_b_product}. This produces {longest_run} primes.')