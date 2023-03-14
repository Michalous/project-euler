result = 0
for a in range (1, 101):
    for b in range(1, 101):
        num = a ** b
        res = sum([int(x) for x in list(str(num))])
        if res > result:
            result = res
print(result)