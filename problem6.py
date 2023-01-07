def sumSquareDifference(n):
    # Takes positive integer n and returns the difference between the sum
    # of the squares of the first n natural numbers and the square of the sum.
    squareOfTheSum = (n*(n+1)/2)**2
    sumOfTheSquares = 0
    for i in range(1, n+1):
        sumOfTheSquares += i**2
    return int(squareOfTheSum - sumOfTheSquares)

if __name__ == "__main__":
    question = 100
    print(sumSquareDifference(question))