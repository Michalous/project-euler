sum_of_all_numbers = 0
facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

for i in range (3, 500000):
	test_num = 0
	for k in range (len(str(i))):
		test_num += facts[int(str(i)[k])]
		if test_num == i:
			print(i)
			sum_of_all_numbers += i
print(sum_of_all_numbers)