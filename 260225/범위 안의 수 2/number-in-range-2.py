res_sum = 0
res_avg = 0
num = 0

for i in range(10):
    n = int(input())

    if 0 <= n and n <= 200:
        res_sum += n
        num += 1

res_avg = res_sum / num

print(f"{res_sum} {res_avg:.1f}")