def maximumPathSum(arr):
    for i in range(len(arr)-2, -1, -1):
        for j in range(0, len(arr[i])):
            if arr[i][j] + arr[i+1][j] >= arr[i][j] + arr[i+1][j+1]:
                arr[i][j] += arr[i+1][j]
            else:
                arr[i][j] += arr[i+1][j+1]
    return arr[0][0]
           
if __name__ == "__main__":
    handle = open("p018.txt", "r")
    triangle = handle.read()
    triangle = triangle.strip().split("\n")
    triangle = [[int(num) for num in row.split()] for row in triangle]

    print(maximumPathSum(triangle))
    


    

