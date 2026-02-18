a, b, c = map(int, input().split())

min_num = 1000

min_num = min(min_num, a)
min_num = min(min_num, b)
min_num = min(min_num, c)

if a == min_num:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b and b == c and a == c:
    print(1)
else:
    print(0)
