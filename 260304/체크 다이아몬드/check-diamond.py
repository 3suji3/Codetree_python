N = int(input())

# 위쪽 (0 ~ N-1)
for i in range(N):
    print(" " * (N - 1 - i) + "* " * (i + 1))

# 아래쪽 (N-2 ~ 0)
for i in range(N - 2, -1, -1):
    print(" " * (N - 1 - i) + "* " * (i + 1))