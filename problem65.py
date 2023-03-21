seq = [2]
convergents = [(2, 1), (3, 1)]

for i in range(33):
    seq += [1, 1, seq[-1] + 2]

for j in seq:
    convergent = (convergents[-1][0] * j + convergents[-2][0], convergents[-1][1] * j + convergents[-2][1])
    convergents.append(convergent)

print(f'result: {sum([int(x) for x in str(convergents[99][0])])}')