a, b = map(int, input().split())

i = a
while i <= b:
    if i % 2 != 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1