def primeFactors(n):
    # Takes in a positive integer and returns an array of its prime factors.
    from math import sqrt
    array = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            n /= i
            array.append(i)
    return array


if __name__ == "__main__":
    question = 600851475143
    print(f"Prime factors of {question} are:")
    print(primeFactors(question))