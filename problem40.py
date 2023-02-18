num = '.'
x = 1
result = 1


for i in range(1, 1000001):
    num += str(i)

for _ in range(1, 7):
    x *= 10
    result *= int(num[x])
print(result)