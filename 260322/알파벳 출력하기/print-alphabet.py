N = int(input())

num = 0  

for i in range(1, N + 1):   # 줄 개수
    for j in range(i):      # i개 출력
        print(chr(num + ord('A')), end='')
        num = (num + 1) % 26
    print()