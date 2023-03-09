from math import factorial

result = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        num = factorial(n)/(factorial(r)*factorial(n-r))
        if num > 10**6:
            result += 1
print(result)