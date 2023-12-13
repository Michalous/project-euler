import math

with open("0099_base_exp.txt", "r") as handle:
        data = handle.read()
data = data.split("\n")

res = [0, 0]
line_no = 0

for line in data:
    line_no += 1
    a = int(line.split(",")[0])
    b = int(line.split(",")[1])
    num = b * math.log(a)
    if num > res[0]:
        res[0] = num
        res[1] = line_no
print(res[1])