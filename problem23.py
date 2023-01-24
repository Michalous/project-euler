import time
from problem21a import sumOfDivisors

def listOfAbundantNumbers():
    abundants = []
    for i in range(12, 28123 - 11):
        if sumOfDivisors(i) > i:
            abundants.append(i)
    return abundants

start = time.time()
combinations = set()
list_of_nums = listOfAbundantNumbers()
for i in range(len(list_of_nums)):
    for j in range(i, len(list_of_nums)):
        if list_of_nums[i] + list_of_nums[j] < 28123:
            combinations.add(list_of_nums[i] + list_of_nums[j])

print(sum(range(28123)) - sum(combinations))
print(f'{time.time() - start} seconds')