def summations(n):
    combs = [1] + [0 for x in range(n)]
    for i in range(n-1):
        for j in range(i+1, n+1):
            combs[j] = combs[j] + combs[j-(i+1)]
    return combs[n]

if __name__ == "__main__":
    print(summations(100))