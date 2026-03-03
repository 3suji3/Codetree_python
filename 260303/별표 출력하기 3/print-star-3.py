N = int(input())

for i in range(N): 
    print("  " * i, end="")
    for k in range(2 * (N - i) - 1):
        print("*", end=" ")
    print()