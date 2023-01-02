import time

def multiples3And5(n):
    # Will find the sum of all the multiples of 3 and 5 below n.
    # Takes positive integer. 
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


if __name__ == "__main__":
    question = 1000
    start = time.time()
    print(multiples3And5(question))
    print(time.time() - start)