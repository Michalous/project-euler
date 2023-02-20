alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0
tri_num_arr = [1]

for i in range(2, 24):
    tri_num_arr.append(tri_num_arr[-1] + i)

with open("p042_words.txt", "r") as handle:
    data = handle.read()
words = [word[1:-1] for word in data.split(',')]

for word in words:
    count = 0
    for i in range(0, len(word)):
        count += alphabet.index(word[i]) + 1
    if count in tri_num_arr:
        res += 1

print(res)