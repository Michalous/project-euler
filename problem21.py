sum_of_amicables = 0

for i in range(5, 10001):
    sum_of_divisors = 0
    potential_amicable = 0
    for j in range(1, int(i/2) + 1):
        if i % j  == 0:
            sum_of_divisors += j
    
    for k in range(1, int(sum_of_divisors / 2) + 1):
        if sum_of_divisors % k == 0:
            potential_amicable += k
            
    if i == potential_amicable:
        if i != sum_of_divisors:
          sum_of_amicables += i

print(f'result: {sum_of_amicables}')