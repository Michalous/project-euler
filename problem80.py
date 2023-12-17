import decimal

result = 0
squares = [4, 9, 16, 25, 36, 49, 64, 81]

for i in range(2, 100):
    if i not in squares:
        x = decimal.Decimal(i)
        dot100 = decimal.Context(prec=105)
        y = str(x.sqrt(dot100))
        result += sum([int(z) for z in y[2:101]]) + int(y[0])
print(result)