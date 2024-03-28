import itertools

with open('0079_keylog.txt', 'r') as handle:
    data = handle.read()
    data = data.split('\n')
    data = data[:-1]

def is_in_order(num_str, permutation):
    return permutation.index(num_str[0]) < permutation.index(num_str[1]) \
        and permutation.index(num_str[1]) < permutation.index(num_str[2])

for permutation in itertools.permutations('01236789'):
    count = 0
    for pin in data:
        count += 1
        if not is_in_order(pin, permutation):
            break
    if count == 50:
        print(''.join(permutation))


