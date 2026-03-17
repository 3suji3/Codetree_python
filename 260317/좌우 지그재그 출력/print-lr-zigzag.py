N = int(input())
num = 1

for i in range(1, N+1):
    if i % 2 != 0:
        for j in range(N):
            print(num,end=" ")
            num += 1
    else:
        num += N
        for j in range(num-1, num-N-1, -1):
            print(j, end=" ")

    print()