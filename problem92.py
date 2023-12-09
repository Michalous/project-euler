# Very slow (takes almost 90 seconds to finish), needs improving
result = 0

def square_digit_chains(num):
    res = 0
    while True:
        for i in range(len(str(num))):
            res += int(str(num)[i]) ** 2
        num = res
        res = 0
        if num == 89 or num == 1:
            return num

for i in range(1, 10000000):
    if square_digit_chains(i) == 89:
        result += 1
print(result)