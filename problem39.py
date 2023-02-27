combinations = dict()

for m in range(1, 22):
    for n in range(1, m):
        for k in range(1, 80):
            a = k * (m**2 - n**2)
            b = k * (2 * m * n)
            c = k * (m**2 + n**2)
            if a + b + c < 1000:
                try:
                    if sorted([a, b, c]) not in combinations[a + b + c]:
                        combinations[a + b + c].append(sorted([a, b, c]))
                except KeyError:
                    combinations[a + b + c] = list()
                    combinations[a + b + c].append(sorted([a, b, c]))

res = max(combinations.values(), key=len)
print(f'The number of solutions is maximised for {sum(res[0])}: {res}')