from problem16 import sumOfTheDigits

def factorialDigitSum(n):
    result = 1
    for i in range(0, n):
        result *= (n - i)
    
    return sumOfTheDigits(result)
    

if __name__ == "__main__":
    question = 100
    print(factorialDigitSum(question))