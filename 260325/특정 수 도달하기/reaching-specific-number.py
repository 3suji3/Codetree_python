nums = []
while len(nums) < 10:
    nums += list(map(int, input().split()))

total = 0
count = 0

for n in nums:
    if n >= 250:
        break
    total += n
    count += 1

print(total, total / count)