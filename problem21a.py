import math 
import time

def sumOfDivisors(num):
    """Takes a positive integer and returns the sum of its divisors"""
    divisors = set()
    divisors.add(1)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(int(num / i))
    return sum(divisors)

def findAmicableNumbers(num):
    """Takes a positive integer num and returns the set of all amicable numbers in a range 1 to num"""
    couples = []
    result = set()
    for i in range(1, num + 1):
        couples.append([i, sumOfDivisors(i)])
    for j in range(len(couples)):
        if [couples[j][1], couples[j][0]] in couples and couples[j][0] != couples[j][1]:
            result.add(couples[j][0])
            result.add(couples[j][1])
    return result

if __name__ == "__main__":
    start = time.time()
    print(sum(findAmicableNumbers(10000)))
    print(time.time() - start)