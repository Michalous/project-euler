result = 0

for i in range(1, 10):
    for j in range(0, 24):
        num = i**j
        if len(str(num)) == j:
            result += 1
print(result)