b, a = map(int, input().split())

i = b

while i > a-1:
    if i % 2 != 0:
        i -= 1
        continue
    print(i, end=" ")
    i -= 1