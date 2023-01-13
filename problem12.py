import math

def numberFactors(n):
    a = 2
    top = math.ceil(math.sqrt(n))
    if top**2 == n:
        a += 1
    for i in range(2, top):
        if n % i == 0:
            a += 2
    return a


if __name__ == "__main__":
    triangle_number = 0
    i = 0
    while True:
        i += 1
        triangle_number += i
        if numberFactors(triangle_number) > 500:
            print(f"{triangle_number}, {numberFactors(triangle_number)}")
            break
