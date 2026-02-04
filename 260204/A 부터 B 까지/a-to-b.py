A, B = map(int, input().split())

print(A, end=" ")

while True:
    if A % 2 == 0:
        if A + 3 >= B:
            break
        A += 3
        print(A, end=" ")
    else:
        if A * 2 >= B:
            break
        A *= 2
        print(A, end=" ")