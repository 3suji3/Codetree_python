N = int(input())

for t in range(2 * N):
    d = min(t, 2 * N - 1 - t)

    if d % 2 == 0:         
        k = 1 + d // 2
    else:                   
        k = N - (d - 1) // 2

    print("* " * k)