a, b = map(int, input().split())

res = a

for i in range(b-1):
    res *= a

print(res)