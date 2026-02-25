N = int(input())

num_sum = 0

for i in range(1, N):
    if N % i == 0:
        num_sum += i

if num_sum == N:
    print('P')
else:
    print('N')