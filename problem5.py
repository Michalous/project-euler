
step = 2*3*5*7*11*13*17*19
num = 0
while True:
    num += step
    b = 0
    for i in range(1, 21):
        if num % i == 0:
            b += 1
    if b == 20:
        break
print(num)