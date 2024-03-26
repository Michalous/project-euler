# slow
from sympy import totient
import time

start = time.time()
res = 0

for i in range(2, 1000001):
    res += totient(i)

print(res)
print(time.time() - start)

# 303963552391