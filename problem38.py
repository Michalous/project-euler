res = 0
q = 0

for num in range(1, 10000):
    con = ''
    z = []

    for i in range(1, 10):
        a = num * i
        con += str(a)
        if len(con) > 9:
            break
        elif len(con) == 9:
            for j in range(0, 9):
                if int(con[j]) == 0:
                    break
                elif con[j] not in z:
                    z.append(con[j])
                    if len(z) == 9:

                        print(con)
                        if int(con) > res:
                            res = int(con)
                            q = num

print(f'reuslut is {res} number to multiply is: {q}')