from problem7 import sieveOfEratosthenes
from math import sqrt

def primeFactors(num):
    arr = sieveOfEratosthenes(int(sqrt(num) + 1))
    res = []
    for prime in arr:
        while num % prime == 0:
            num /= prime
            res.append(prime)
    if num != 1:
        res.append(int(num))
    return res

if __name__ == '__main__':
    print(primeFactors(600851475143))