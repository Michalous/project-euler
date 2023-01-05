def isPalindrome(n):
    # Checks if the integer is a palindrome and returns True if it is.
    for i in range(int(len(str(n))/2)+1):
        if str(n)[i] != str(n)[-1-i]:
            return False
    return True


def largestPalindromeProduct(n):
    # Looks for the greatest palindrome made from the product of two n-digit numbers  
    # and returns an array consisting of the palindrome and those two numbers.
    result = 0
    arr = []
    for i in range(10**(n-1), 10**(n)):
        for j in range(10**(n-1), 10**(n)):
            if isPalindrome(i*j) and result < i*j:
                result = i*j
                arr = [result, i, j]
    return arr

if __name__ == "__main__":
    question = 3
    print(largestPalindromeProduct(question))