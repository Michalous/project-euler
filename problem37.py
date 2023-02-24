from problem7 import sieveOfEratosthenes

prms = sieveOfEratosthenes(750000)
primes = set(prms)

left = set()
for prime in primes:
  p = str(prime)
  pr = ''
  for digit in range(len(p)):
    pr += p[digit]
    if int(pr) not in primes:
      break
    if len(pr) == len(str(prime)):
        left.add(prime)

right = []
for num in left:
  p = str(num)
  pr = ''

  for z in range(len(p)):
    pr = p[z:]

    if int(pr) not in primes:
      break
    if num not in right:
      if len(pr) == 1:
        right.append(num)

print(f'result: {sum(right) - (2 + 3 + 5 + 7)}')