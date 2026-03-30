num_list = list(map(int, input().split()))

two = 0
three = 0
t_cnt = 0

for idx in range(10):  
    if (idx + 1) % 2 == 0:   
        two += num_list[idx]
        
    if (idx + 1) % 3 == 0: 
        three += num_list[idx]
        t_cnt += 1

three = three / t_cnt

print(f"{two} {three:.1f}")