#6857 - 4/10/24

number = 600_851_475_143
possibles = []
primes = []

i = 3
n = number

while i <= n:
  if (number % i == 0):
    n = number / i
    possibles.append(i)
  i += 2
print(possibles)

def isPrime(num):
  for i in range(2, num):
    if (num % i == 0):
      return(False)
  return(True)

for i in range(len(possibles)):
  if (isPrime(possibles[i])):
    primes.append(possibles[i])

print(primes)