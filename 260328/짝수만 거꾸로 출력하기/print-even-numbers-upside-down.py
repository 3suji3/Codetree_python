N = int(input())

N_list = list(map(int, input().split()))

two_num = 0

for i in range(N-1, -1, -1):
    if N_list[i] % 2 == 0:
        two_num += 1
        print(N_list[i], end=" ")

if two_num == 0:
    print(0)