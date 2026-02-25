a, b = map(int, input().split())

res_sum = 0
res_avg = 0
num = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        res_sum += i
        num+=1

res_avg = res_sum / num

print(f"{res_sum} {res_avg:.1f}")