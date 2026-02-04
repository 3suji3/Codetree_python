N = int(input())
number_sum = 0

for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if j % 2 == 0:
            number_sum += j
    print(number_sum)
    number_sum = 0