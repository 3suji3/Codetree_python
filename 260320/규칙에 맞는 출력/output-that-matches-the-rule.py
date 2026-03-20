N = int(input())

for i in range(N, 0, -1): 
    for j in range(1, N+1): 
        if i - j <= 0: 
            print(j, end =" ") 
    print()