N, a = map(int, input().split())

i = 0

while i < N:
    i+=1
    if i % a == 0:
        print(1)
    else:
        print(0)