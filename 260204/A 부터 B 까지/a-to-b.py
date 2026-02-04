A, B = map(int, input().split())

print(A, end=" ")
val = A
while True:
    if A % 2 == 0:
        val += 3
    else:
        val *= 2
    
    if val > B:
        break
    A = val
    
    print(A, end=" ")