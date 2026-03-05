N = int(input())

arr = []

for i in range(N):
    if i % 2 == 0:
        arr.append(N - i//2)
    else:
        arr.append(1 + i//2)

for x in arr:
    print("* " * x)

for x in reversed(arr):
    print("* " * x)