import math

def continued_fraction_sqrt(D):
    m = 0
    d = 1
    a0 = a = int(math.sqrt(D))
    
    coefficients = [a0]

    if a * a == D:
        return coefficients  # If D is a perfect square, the expansion terminates.

    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        coefficients.append(a)
        
        if a == 2 * a0 and coefficients.count(a) == 2:
            return coefficients[:-1]
        if a == 2 * a0 and len(coefficients) % 2 == 1:
            return coefficients
        

def find_fundamental_solution_from_cf(D):
    coefficients = continued_fraction_sqrt(D)
    
    # Convergents
    p_prev2, p_prev1 = 1, coefficients[0]
    q_prev2, q_prev1 = 0, 1
    
    for a in coefficients[1:]:
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        
        if p * p - D * q * q == 1:
            return p, q
        
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q

result = [0, 0]
for i in range(1, 1001):
    a = find_fundamental_solution_from_cf(i)
    if a is not None:
        if a[0] > result [1]:
            result[0] = i
            result[1] = a[0]

print(result)