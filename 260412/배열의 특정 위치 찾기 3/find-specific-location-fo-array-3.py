n_list = list(map(int, input().split()))
result = 0
for i in n_list:
    if i == 0:
        break
    result += i

print(result)