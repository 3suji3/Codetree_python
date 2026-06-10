arr = list(map(int, input().split()))
twos = 0
ones = 0

for i in range(0, len(arr), 2):
    twos += arr[i]

for i in range(1, len(arr), 2):
    ones += arr[i]

if twos >= ones:
    print(twos-ones)
else:
    print(ones-twos)