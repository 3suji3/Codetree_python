N = int(input())

for i in range(0, N):
    if (i+1) % 2 != 0:
        print("*", end=" ")
    else:
        for j in range(i+1):
            print("*", end=" ")
    print()