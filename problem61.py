triangle = [(3, int(x*(x + 1) / 2)) for x in range(18, 141) if x*(x + 1) / 2 > 999 and x*(x + 1) /2 < 10000]
square = [(4, x**2) for x in range(18, 141) if x**2 > 999 and x**2 < 10000]
pentagonal = [(5, int(x*(3*x - 1) / 2))for x in range(18, 141) if int(x*(3*x - 1) / 2) > 999 and int(x*(3*x - 1) / 2) < 10000]
hexagonal = [(6, int(x*(2*x - 1))) for x in range(18, 141) if int(x*(2*x - 1)) > 999 and int(x*(2*x - 1)) < 10000]
heptagonal = [(7, int(x*(5*x - 3) / 2)) for x in range(18, 141) if int(x*(5*x - 3) / 2) > 999 and int(x*(5*x - 3) / 2) < 10000]
octagonal = [(8, int(x*(3*x - 2))) for x in range(18, 141) if int(x*(3*x - 2)) > 999 and int(x*(3*x - 2)) < 10000]

arr = triangle + square + pentagonal + hexagonal + heptagonal + octagonal

dict_of_tuples = dict()

for x in arr:
    temp_arr = []
    for y in arr:
       if str(x[1])[2:] == str(y[1])[0:2] and str(y[1])[2] != '0':
           temp_arr.append(y)
    if len(temp_arr) > 0:
        dict_of_tuples[x] = temp_arr
 
    
flag = True
for a in dict_of_tuples:
    if not flag:
        break
    for b in dict_of_tuples[a]:
        for c in dict_of_tuples[b]:
            for d in dict_of_tuples[c]:
                for e in dict_of_tuples[d]:
                    for f in dict_of_tuples[e]:
                       test = set([a[0], b[0], c[0], d[0], e[0], f[0]])
                       if len(test) == 6 and str(f[1])[2:] == str(a[1])[0:2]:
                           print(a,b,c,d,e,f)
                           print(sum([x[1] for x in [a,b,c,d,e,f]]))
                           flag = False
                           break














