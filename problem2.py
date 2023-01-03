def fibonacciGenerator():
    '''Generates Fibonacci numbers '''
    array = [0, 1]
    while True:
        yield array[-1]
        array.append(array[-1] + array[-2])
    
def evenFibCount(num):
    '''
    Takes integer num > 1
    Returns the sum of even-valued terms
    in Fibonacci sequence whose values don't exceed num. 
    '''
    fib_num = fibonacciGenerator()
    x = 0
    result = 0
    while x < num:
        if x % 2 == 0:
            result += x
        x = fib_num.__next__()
    return result

if __name__ == "__main__":
    question = 4000000
    print(evenFibCount(question))
   