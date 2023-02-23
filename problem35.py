from problem7 import sieveOfEratosthenes

primes = sieveOfEratosthenes(1000000)
bad_digits = [2, 4, 5, 6, 8, 0]
result = 2 # for 2 and 5 that are in bad_digits

for num in primes:
    for i in range(len(str(num))):
        if int(str(num)[i]) in bad_digits:
            primes.remove(num)
            break 

for x in primes:
	count = 0
	p = x
	for i in range(len(str(x))):
		p = str(p)[-1] + str(p)[:-1]
		if int(p) not in primes:
			break
			
		count += 1
	if count == len(str(x)):
		result += 1
		print(x)
print(f'Result: {result}')