on_diagonal = 1
step = 0
sum_of_diagonals = 1


while on_diagonal < 1001 * 1001:
	step += 2
	for _ in range(1, 5):
		on_diagonal = on_diagonal + step
		sum_of_diagonals = sum_of_diagonals + on_diagonal
	
print(sum_of_diagonals)