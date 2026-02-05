sum = 0
number = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    for j in range(4):
        sum = number[i][j] + sum
    print(sum)
    sum = 0