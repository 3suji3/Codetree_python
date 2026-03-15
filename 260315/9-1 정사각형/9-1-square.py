N = int(input())
cnt = 9

for i in range(N):
    for j in range(N):
        if cnt < 1:
            cnt = 9
        print(cnt, end="")
        cnt -= 1
    print()