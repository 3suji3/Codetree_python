a, b, c = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if i % c == 0:
        print('YES')
        break
    cnt += 1
else:
    print("NO")