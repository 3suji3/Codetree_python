num_list = list(map(int, input().split()))

two = 0
three = 0
t_cnt = 0

for i in num_list:
    if i % 2 == 0:
        two += i
    if i % 3 == 0:
        three += i
        t_cnt += 1

three = three / t_cnt

print(f"{two} {three:.1f}")