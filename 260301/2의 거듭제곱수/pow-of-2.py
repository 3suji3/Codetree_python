n = int(input())
cnt = 0
i = 1

while True:
    if i >= n:
        break
    i *= 2
    cnt +=1

print(cnt)