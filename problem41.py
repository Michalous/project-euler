# 9 & 8 pandigital numbers are divisible by 3 so none of them is prime

from itertools import permutations
from sympy.ntheory import isprime

def rSubset(arr, r):
    return list(permutations(arr, r))

arr = [7, 6, 5, 4, 3, 2, 1]
r = 7

for x in rSubset(arr, r):
    z = ''
    for q in range(0, 7):
        z += str(x[q])
    if isprime(int(z)):
        print(f'The biggest pandigital prime is: {z}')
        break