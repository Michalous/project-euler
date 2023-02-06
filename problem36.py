n = 0
for i in range (1, 1000001):
	rev = str(i)[::-1]
	if i - int(rev) == 0:
		bi = (bin(i)[2:])
		bi_rev = str(bi)[::-1]
		if int(bi) - int(bi_rev) == 0:
			n = n + i
			print('binary of ' + str(i) + ' is: ' + bi)
print('=======')
print('sum of all palindromes in binary/decimal base less than 1000000 is: ' + str(n))