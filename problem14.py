import copy
import time
start_time = time.time()


def collatz(n, memo = {2: 2}):
    a = copy.deepcopy(n)
    arr = [n]
    while n > 1:
        try:
            answer =  memo[int(n)] + len(arr[:-1])
            break
        except KeyError:        
            if n % 2 == 0:
                n /= 2
                arr.append(int(n))               
            else:
                n = 3 * n + 1
                arr.append(int(n))
    try:
        memo[a] = answer
    except (ValueError, RuntimeError, TypeError, NameError):
        answer = len(arr)
        memo[a] = answer
    
    for i in range(len(arr)):
        try:
            memo[int(arr[i])] = memo[int(arr[i])]
            break
        except KeyError:
            memo[int(arr[i])] = len(arr[i:])
    return answer

result = [0, 0]

for i in range(1000001):
    if collatz(i) > result[0]:
        result[0] = collatz(i)
        result[1] = i
print(result)
print("--- %s seconds ---" % (time.time() - start_time))


























