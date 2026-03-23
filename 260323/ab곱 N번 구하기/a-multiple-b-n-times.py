N = int(input())

n_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    res = 1
    for j in range(n_list[i][0], n_list[i][1] + 1):
        res *= j
    print(res)