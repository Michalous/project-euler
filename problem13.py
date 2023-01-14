

file = open('p013.txt', 'r')
arr = file.read()
arr = arr.split('\n')

result = 0
for i in range(0, 100):
    result += int(arr[i])
print(str(result)[0:10])

