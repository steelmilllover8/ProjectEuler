results = []
palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        results.append(i * j)
print("--Done--")

def isPeleindrome(n):
    numberfor = []
    numberbac = []
    while (n > 1):
        numberfor.append(int(n % 10))
        n /= 10
    for i in range(1, len(numberfor) + 1):
        numberbac.append(numberfor[len(numberfor) - i])

    for i in range( len(numberfor)):
        if (numberfor[i] != numberbac[i]):
            return(False)
    return(True)
        
for i in range(len(results)):
    if (isPeleindrome(results[i])):
        palindromes.append(results[i])

largest = -1
for i in range(len(palindromes)):
    if (palindromes[i] > largest):
        largest = palindromes[i]

print(largest)