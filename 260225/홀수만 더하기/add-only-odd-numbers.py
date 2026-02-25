n = int(input())

res = 0

for i in range(n):
    num = int(input())
    if num % 2 != 0 and num % 3 == 0:
        res += num

print(res)