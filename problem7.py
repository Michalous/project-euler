def sieveOfEratosthenes(n):
    # Takes N and returns a list of primes less than N (starting with 2 at index 0).
    from math import sqrt
    array = list(range(n))
    
    for i in range(2, int(sqrt(n) + 1)):
        if array[i] !=0:
            array[i*i] = 0
            j = i
            while ((i*i) + j) < n:
                array[(i*i) + j] = 0
                j += i
        
    listOfPrimes = []
    for k in range(2, len(array)):
        if array[k] != 0:
            listOfPrimes.append(array[k])
    return listOfPrimes


if __name__ == "__main__":
    question = 10001
    print(sieveOfEratosthenes(150000)[question - 1])
