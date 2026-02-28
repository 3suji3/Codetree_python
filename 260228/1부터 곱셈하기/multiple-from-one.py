n = int(input())

res = 1

for i in range(1, n+1):
    if res < n:
        res *= i
    else:
        res = i - 1
        break
print(res)
