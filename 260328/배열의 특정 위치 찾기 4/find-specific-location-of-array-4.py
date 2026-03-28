ten = list(map(int, input().split()))
res_two = 0
sum_two = 0
for i in ten:
    if i == 0:
        break
    if i % 2 == 0:
        res_two += 1
        sum_two += i

print(f"{res_two} {sum_two}")