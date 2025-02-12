n=int(input("Enter the number of rows: "))

for r in range(1, n+1):
    for c in range(r):
        print("-_-", end=" ")
    print()
