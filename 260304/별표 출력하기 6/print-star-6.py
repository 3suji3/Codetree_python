N = int(input())

for i in range(N, 0, -1):
    for j in range((N-i) * 2):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print("*", end=" ")
    print()

for i in range(1, N):
    for j in range((N-i-1) * 2):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end=" ")
    print()