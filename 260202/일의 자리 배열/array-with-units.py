N, M = map(int, input().split())

a = [N, M]

num = 0

for i in range(2, 10):
    num = a[i-2] + a[i-1] 
    if num > 9:
        num = num % 10
    a.append(num)

print(*a)