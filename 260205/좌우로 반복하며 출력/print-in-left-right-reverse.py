n = int(input())

for i in range(n):
    row = []
    
    for j in range(1, n+1):
        row.append(j)

    if i % 2 != 0:
        for j in range(n - 1, -1, -1):
            print(row[j], end="")
    else:
        for j in range(n):
            print(row[j], end="")
    
    print()
