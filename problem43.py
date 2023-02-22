import itertools
result = 0

for p in itertools.permutations('0123456789'):
    if int(p[1] + p[2] + p[3]) % 2 == 0:
        if int(p[2] + p[3] + p[4]) % 3 == 0:
            if int(p[3] + p[4] + p[5]) % 5 == 0:
                if int(p[4] + p[5] + p[6]) % 7 == 0:
                    if int(p[5] + p[6] + p[7]) % 11 == 0:
                        if int(p[6] + p[7] + p[8]) % 13 == 0:
                            if int(p[7] + p[8] + p[9]) % 17 == 0:
                                result += int(''.join(str(x) for x in p))
                                print(p)
print(result)