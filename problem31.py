count = 1 # option with 1 £2 coin

for a in range(200, -100, -100):
  if a == 200:
    count += 1
  if a < 200:
    for b in range(200, -50, -50):
      if a + b == 200:
        count += 1
      if a + b < 200:
        for c in range(200, -20, -20):
          if a + b + c == 200:
            count += 1
          if a + b + c < 200:
            for d in range(200, -10, -10):
              if a + b + c + d == 200:
                count += 1
              if a + b + c + d < 200:
                for e in range(200, -5, -5):
                  if a + b + c + d + e == 200:
                    count += 1
                  if a + b + c + d + e < 200: 
                    for f in range(200, -2, -2):
                      if a + b + c + d + e + f == 200:
                        count += 1
                      if a + b + c + d + e + f < 200:
                        for g in range(200, -1, -1):
                          if a + b + c + d + e + f + g == 200:
                            count += 1
print(count)