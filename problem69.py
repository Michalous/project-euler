from problem3a import primeFactors

def totient_function(num):
    set_of_primes = set(primeFactors(num))
    result = num
    for prime in set_of_primes:
        result *= (1 - (1 / prime))
    return int(result)

if __name__ == '__main__':
    guess = 2 * 3 * 5 * 7 * 11 * 13 * 17
    print(guess / totient_function(guess))