n = int(input())

for i in range(n):
    a = i + 1
    b = n - i
    for j in range(n):
        if j % 2 == 0:
            print(a, end="")
        else:
            print(b, end="")
    print()
