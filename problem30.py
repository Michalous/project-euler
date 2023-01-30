result = 0
for i in range(10, 1000000):
    sum_of_powers = 0
    for x in str(i):
        sum_of_powers += int(x)**5
    if sum_of_powers == int(i):
        result += i

print(result)