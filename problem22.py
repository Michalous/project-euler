alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("p022_names.txt", "r") as handle:
    data = handle.read()
names = [name[1:-1] for name in data.split(',')]
names.sort()
res = 0
for name in names:
    count = 0
    for i in range(0, len(name)):
        count += alphabet.index(name[i]) + 1
    res += (names.index(name) + 1) * count
print(res)

