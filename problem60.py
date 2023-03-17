from problem7 import sieveOfEratosthenes
from sympy.ntheory import isprime

primes = sieveOfEratosthenes(10000)

isTrue = True

for pn in primes:
    if not isTrue:
        break
    res_arr = [pn]
    for prime in primes:
        temp = []
        for num in res_arr:
            if isprime(int(str(prime) + str(num))) == True and isprime(int(str(num) + str(prime))) == True:
                temp.append(prime)
        if len(temp) == len(res_arr):
            res_arr.append(prime)
        if len(res_arr) == 5:
            print(res_arr)
            print(f'Result: {sum(res_arr)}')
            isTrue = False
            break