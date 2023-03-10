from problem18 import maximumPathSum

handle = open("p067.txt", "r")
triangle = handle.read()
triangle = triangle.strip().split("\n")
triangle = [[int(num) for num in row.split()] for row in triangle]

print(maximumPathSum(triangle))