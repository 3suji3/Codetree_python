res = 0
cnt = 0

while True:
    n = int(input())
    if n > 29:
        res /= cnt
        break
    cnt += 1
    res += n

print(f"{res:.2f}")