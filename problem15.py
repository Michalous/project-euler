import math
result = []

for i in range(1, 15):
    triangle = []
    for j in range(0, i + 1):
        a = math.factorial(i)/(math.factorial(j)*math.factorial(i - j))
        triangle.append(int(a))

    print(triangle)

    if len(triangle) % 2 != 0:
        triangle.sort()
        result.append(triangle[-1])

print(f'Result: {result}')