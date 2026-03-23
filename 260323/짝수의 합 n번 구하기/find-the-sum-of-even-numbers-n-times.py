N = int(input())
n_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    a, b = n_list[i]
    res = 0
    
    for j in range(a, b + 1):
        if j % 2 == 0:
            res += j
    
    print(res)