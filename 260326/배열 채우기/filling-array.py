nums = list(map(int, input().split()))

result = []

for n in nums:
    if n == 0:
        break
    result.append(n)

# 역순 출력
for n in reversed(result):
    print(n, end=' ')