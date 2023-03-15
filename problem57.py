numerator = 3
denominator = 2
temp = 2
result = 0
for i in range(1, 1000):
    denominator += numerator
    numerator = temp + denominator
    temp = denominator
    if len(str(numerator)) > len(str(denominator)):
        result += 1 
print(result)