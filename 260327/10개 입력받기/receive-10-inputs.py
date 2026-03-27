nums = list(map(int, input().split()))

total = 0
count = 0

for n in nums:
    if n == 0:
        break
    total += n
    count += 1

avg = total / count

print(total, f"{avg:.1f}")