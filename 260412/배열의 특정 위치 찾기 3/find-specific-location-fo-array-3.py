n_list = list(map(int, input().split()))
result = 0
for i in range(len(n_list)):
    if n_list[i] == 0:
        result = n_list[i-3] + n_list[i-2] + n_list[i-1]
        break

print(result)