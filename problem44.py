from math import sqrt

pentagonal_numbers = set([1, 5])

def isPentagonal(n):
    return (1 + sqrt(1 + 24*n)) % 6 == 0

if __name__ == "__main__":
    x = 4
    num = 5
    isTrue = True

    while isTrue:
        x += 3
        num += x
        for pn in pentagonal_numbers:
            if isPentagonal(abs(pn - num)) and isPentagonal(pn + num):
                print(abs(pn - num))
                isTrue = False
                break
        pentagonal_numbers.add(num)  