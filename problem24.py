import itertools
idx = 0

for permutation in itertools.permutations('0123456789'):
	idx +=  1
	
	if idx == 1000000:
		print(permutation)