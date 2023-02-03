result =[]

for i in range(1, 99):
  for j in range(123, 9877):
    test_set = set()
    prod = i * j
    test_string = str(prod) + str(i) + str(j)
    
    if len(test_string) == 9 and '0' not in test_string:
      for digit in test_string: 
          test_set.add(digit)
          
    if len(test_set) == 9:
      if prod not in result:
        result.append(prod)
        print(f'{i} x {j} = {prod}')
           
print(sum(result))