from problem7 import sieveOfEratosthenes

primes = sieveOfEratosthenes(1000000)
prms = set(primes) 

result = [0, 0] # prime, length

for i in range(0, 1000): # starting at 1000th prime would only generate a sum of 117 consecutive primes below 1000000
    for j in range(i, len(primes)):
        x = sum(primes[i:j])
        if x > 1000000:
            break
        if x in prms:
            if (j - i) > result[1]:
                result = [x, j - i]
print(result)