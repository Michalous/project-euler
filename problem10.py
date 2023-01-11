from problem7 import sieveOfEratosthenes

def sumOfPrimesBelowN(n):
    return sum(sieveOfEratosthenes(n))

if __name__ == "__main__":
    question = 2000000
    print(sumOfPrimesBelowN(question))