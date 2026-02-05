arr = [list(map(int, input().split())) for _ in range(3)]
input()
arg = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        number = arr[i][j] * arg[i][j]
        print(number, end=" ")
    print()