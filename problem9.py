def pythagoreanTriplets():
    array = [0]
    for i in range(1, 500):
        array.append(i*i)
    
    for a in range(1, 499):
        for b in range(a, 499):
            if array[a] + array[b] in array:
                c = array.index(array[a] + array[b])
                if a + b + c == 1000:
                    print(f"{a} + {b} + {c} = {a + b + c}")
                    print(f"{a * a} + {b * b} = {c * c}")

pythagoreanTriplets()
