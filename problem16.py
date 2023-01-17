def sumOfDigits(num):
    return sum([int(x) for x in str(num)])

if __name__ == "__main__":
    question = 2**1000
    print(sumOfDigits(question))