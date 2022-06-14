# 4.4. break and continue Statements, and else Clauses on Loops

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop jatuh tanpa menemukan faktor
        print(n, 'is a prime number')

print("")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)