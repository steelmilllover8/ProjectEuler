number = 2

def SmallestDivisible(n):
  for i in range(1, 21):
    if (n % i != 0):
      return(False)
    
while (SmallestDivisible(number) == False):
  print(number)
  number += 2
  SmallestDivisible(number)

