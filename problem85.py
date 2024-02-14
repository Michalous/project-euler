# Triangular numbers (x**2 + x) / 2, (y**2 + y) / 2
res = [100000, 0, 0]
for x in range(1, 100):
    for y in range(x + 1, 100):
        z = (x*y/4)*(x+1)*(y+1)
        if abs(2000000 - z) < res[0]:
            res = [abs(2000000 - z), x, y, x*y]
print(res)