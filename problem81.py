with open('0081_matrix.txt', 'r') as handle:
    data = handle.read()


data = data.strip().split("\n")
data = [[int(num) for num in row.split(',')] for row in data]

half_matrix = []
triangle = []

def minimumPathSum(arr):
    for i in range(len(arr)-2, -1, -1):
        for j in range(0, len(arr[i])):
            if arr[i][j] + arr[i+1][j] <= arr[i][j] + arr[i+1][j+1]:
                arr[i][j] += arr[i+1][j]
            else:
                arr[i][j] += arr[i+1][j+1]
    return arr[0][0]

for i in range(len(data)):
    to_append = []
    for j in range(i+1):
        to_append.append(data[i-j][j])
    half_matrix.append(to_append)

for i in range(len(data) - 1):
    to_append = []
    for j in range(i+1):
        to_append.append(data[len(data) - 1 - j][len(data) - 1 - i + j])
    
    triangle.append(to_append)

for i in range(1, len(half_matrix)):
    half_matrix[i][0] += half_matrix[i-1][0]
    half_matrix[i][-1] += half_matrix[i-1][-1]

for i in range(2, len(half_matrix)):
    for j in range(1, len(half_matrix[i]) -1):
        if half_matrix[i-1][j-1] < half_matrix[i-1][j]:
            half_matrix[i][j] += half_matrix[i-1][j-1]
        else:
            half_matrix[i][j] += half_matrix[i-1][j]

triangle.append(half_matrix[len(data) - 1])
print(minimumPathSum(triangle))