from math import sqrt
from problem44 import isPentagonal

def isTriangle(n):
    return (sqrt(1 + 8 * n) -1) % 2 == 0

hex_num = 6
x = 9

while True:
    hex_num += x
    x += 4
    if isPentagonal(hex_num):
        if isTriangle(hex_num):
            if hex_num > 40755:
                print(hex_num)
                break