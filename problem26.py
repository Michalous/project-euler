import math

def recurring_cycle(denom, numer=1):
    cycle = []
    while True:
        while numer < denom:
            numer *= 10
            if (0, numer % denom) in cycle:
                return len(cycle) - cycle.index((0, numer % denom))
            cycle.append((0, numer % denom))
        
        remainder = numer % denom
        if remainder == 0:
            return 0
        if (math.floor(numer / denom), remainder) in cycle:
            return len(cycle) - cycle.index((math.floor(numer / denom), remainder))
        cycle.append((math.floor(numer / denom), remainder))
        numer = remainder
        numer *= 10

if __name__ == "__main__":   
    result = 0
    longest_cycle = 0
    
    for i in range(1, 1001):
        if recurring_cycle(i) > longest_cycle:
            result = i
            longest_cycle = recurring_cycle(i)
 
    print(f'The longest recurring cycle has {longest_cycle} digits. Value of d is: {result}')
            