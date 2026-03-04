N = int(input())

# 위쪽
for i in range(1, N+1):
    for j in range((N-i)*2):
        print(" ", end="")
    for j in range(i):
        print("@", end=" ")
    print()

# 아래쪽
for i in range(N-1, 0, -1):
    for j in range(i):
        print("@", end=" ")
    print()