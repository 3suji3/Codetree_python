A, B = map(int, input().split())

print(A, end=" ")

while True:
    if A >= B:
        break
    if A % 2 == 0:
        A += 3
        print(A, end=" ")
    else:
        A *= 2
        print(A, end=" ")