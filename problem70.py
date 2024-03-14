from problem7 import sieveOfEratosthenes

result = [1000, 0, 0, 0]

def isPerumutation(num1, num2):
    n1 = sorted([x for x in str(num1)])
    n2 = sorted([x for x in str(num2)])
    return n1 == n2

primes = sieveOfEratosthenes(8000)

for i in range(len(primes)):
    for j in range(len(primes)):
        num = primes[i] * primes[j]
        if num < 10**7:
            if i == j:
                totient = (primes[i] - 1) * primes[j]
            else:
                totient = (primes[i] - 1) * (primes[j] - 1)
            if isPerumutation(num, totient) and (num / totient < result[0]):
                result[0] = num / totient
                result[1] = num
                result[2] = primes[i]
                result[3] = primes[j]
print(f'result = {result[1]}')
print(result)
            
        



    