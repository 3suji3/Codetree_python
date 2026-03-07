N = int(input())

size = 2 * N + 1

for i in range(size):          # 행
    for j in range(size):      # 열
        if i % 2 == 0 or j % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()