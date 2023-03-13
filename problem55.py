result = 0

for i in range(1, 10001):
    iter = 0
    num = i
    while iter < 50:
        iter += 1
        revnum = int(str(num)[::-1])
        a = num + revnum
        if a - int(str(a)[::-1]) == 0:
            result += 1
            break
        num = a

print(10000 - result)