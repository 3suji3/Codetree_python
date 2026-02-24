A, B = map(int, input().split())

i = A
print(i, end=" ")

while True:
    if i % 2 == 0:
        i += 3
        if i > B:
            break
        else:
            print(i, end=" ")
    else:
        i *= 2
        if i > B:
            break
        else:
            print(i, end=" ")