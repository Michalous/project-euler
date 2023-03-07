from problem7 import sieveOfEratosthenes

primes1, primes2 = sieveOfEratosthenes(1000000), sieveOfEratosthenes(100000)
primes_set = set(primes1) - set(primes2) # it doesn't have to be ordered

result = []

isTrue = True

for prime in primes_set:
    if not isTrue:
        break
    ceil = len(str(prime))
    for i in range(ceil - 2):
        for j in range(i + 1, ceil):
            for k in range(i + 2, ceil):
                num = list(str(prime))
                sum_a = []
                for x in range(0, 10):
                    num[i] = x
                    num[j] = x
                    num[k] = x
                    newNum = int(''.join(str(z) for z in num))
                    if newNum in primes_set:
                            sum_a.append(newNum)
                if len(sum_a) == 8:
                    result = sum_a
                    isTrue = False
                    break 
print(result)
print(f'Result: {result[0]}')                 