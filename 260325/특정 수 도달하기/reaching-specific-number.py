nums = []
while len(nums) < 10:
    nums += list(map(int, input().split()))

s = 0
cnt = 0

for x in nums:
    if x >= 250:
        break
    s += x
    cnt += 1

print(s, round(s / cnt, 1))