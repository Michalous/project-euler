from fractions import Fraction

numerator = 1
denumerator = 1

for i in range(10, 100):
  for j in range(i + 1, 100):
    test_num = str(i)
    test_den = str(j)
    
    if test_num[0] == test_den[1]:  
      a = int(test_num[1])
      b = int(test_den[0])
      if a / b == i / j:
        numerator *= a
        denumerator *= b
      
    elif test_num[1] == test_den[0]:
      a = int(test_num[0])
      b = int(test_den[1])
      if b != 0:
        if i / j == a/b:
          numerator *= a
          denumerator *= b
          print(f'{i}/{j}')
          print(f'{a}/{b}')
          print('=======')
          
          
print(f'Result: {numerator}/{denumerator}')
print(f'Result in its lowest common terms: {Fraction(numerator, denumerator)}')