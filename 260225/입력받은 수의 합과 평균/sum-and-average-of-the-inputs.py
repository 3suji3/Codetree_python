N = int(input())

res_sum = 0
res_avg = 0

for i in range(N):
    n = int(input())
    res_sum += n

res_avg = res_sum / N

print(f"{res_sum} {res_avg:.1f}")