N, M = map(int, input().split())

# Please write your code here.

while N > 0:
    print(int(N))
    if N < 1:
        break
    N //= M
    