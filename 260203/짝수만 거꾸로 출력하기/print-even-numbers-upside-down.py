N = int(input())
arr = []
j = list(map(int, input().split()))

for i in j:
    if i % 2 == 0:
        arr.append(i)

for x in arr[::-1]:
    print(x, end=" ")
