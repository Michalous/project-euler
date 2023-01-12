file = open("p011.txt", "r")
arr = file.read()
arr = arr.strip().split('\n')
arr = [[int(num) for num in row.split()] for row in arr]

result = 0
# line count
for i in range(0, 20):
    for j in range(0,17):
        product = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
        if product > result:
            result = product

# column count
for i in range(0, 17):
    for j in range(0, 20):
        product = arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j]
        if product > result:
            result = product

# diagonal top to right bottom
for i in range(0, 17):
    for j in range(0, 17):
        product = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
        if product > result:
            result = product

# diagonal top to left bottom
for i in range(0, 17):
    for j in range(3, 20):
        product = arr[i][j] * arr[i+1][j-1] * arr[i+2][j-2] * arr[i+3][j-3]
        if product > result:
            result = product

print(result)