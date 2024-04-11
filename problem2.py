total = 0
def fibonacci(num1, num2):
  temp = num2
  num2 = (num1 + num2)
  num1 = temp

  if num2 < 4_000_000:
    if (num2 % 2 == 0):
      global total
      total += num2
    fibonacci(num1, num2)

fibonacci(1,2)
print(total + int(2))