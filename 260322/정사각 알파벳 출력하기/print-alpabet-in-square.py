N = int(input())

start = ord('A')  

for i in range(N):
    for j in range(N):
        print(chr(start), end='')
        start += 1
    print()