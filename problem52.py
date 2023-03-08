start = 1
multiples = [2, 3, 4, 5, 6]
isTrue = True

while isTrue:
    start *= 10
    end = int(start * 1.6) + 1
    for i in range(start, end):
        x = list(str(i))
        count = 0
        notDigit = False
        for multiple in multiples:
            if notDigit:
                break 
            test = list(str(i * multiple))
            for digit in test:
                if digit not in x:
                    notDigit = True
                    break
            count += 1
        if count == 5:
            print([i, i*2, i*3, i*4, i*5, i*6])
            isTrue = False