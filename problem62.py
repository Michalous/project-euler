numbers = dict()
i = 0
while True:
    i += 1
    num = sorted(list(str(i**3)), reverse=True)
    num = int("".join(num))
    try:
        numbers[num].append(i)
        if len(numbers[num]) == 5:
            print(numbers[num])
            print(f'smallest cube is: {numbers[num][0]**3}')
            break
    except KeyError:
        numbers[num] = [i]  