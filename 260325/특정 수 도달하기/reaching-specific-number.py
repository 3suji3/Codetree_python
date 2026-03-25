nums = list(map(int, input().split()))

result = []

for n in nums:
    if n >= 250:
        break
    result.append(n)

total = sum(result)
avg = total / len(result)

print(total, avg)