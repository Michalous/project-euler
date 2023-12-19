import itertools
import time

start = time.time()

result = []
for permutation in itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
    
    a = [int(permutation[0]), int(permutation[1]), int(permutation[2])]
    b = [int(permutation[3]), int(permutation[2]), int(permutation[4])]
    c = [int(permutation[5]), int(permutation[4]), int(permutation[6])]
    d = [int(permutation[7]), int(permutation[6]), int(permutation[8])]
    e = [int(permutation[9]), int(permutation[8]), int(permutation[1])]
    
    if sum(a) == sum(b) == sum(c) == sum(d) == sum(e):
        smallest = min([a[0], b[0], c[0], d[0], e[0]])
        if a[0] == smallest:
            if a+b+c+d+e not in result:
                result.append(a+b+c+d+e)
        elif b[0] == smallest:
            if b+c+d+e+a not in result:
                result.append(b+c+d+e+a)
        elif c[0] == smallest:
            if c+d+e+a+b not in result:
                result.append(c+d+e+a+b)
        elif d[0] == smallest:
            if d+e+a+b+c not in result:
                result.append(d+e+a+b+c)
        else:
            if e+a+b+c+d not in result:
                result.append(e+a+b+c+d)
print(''.join(str(x) for x in max(result)))
print('time: ' + str(time.time() - start) + 's')