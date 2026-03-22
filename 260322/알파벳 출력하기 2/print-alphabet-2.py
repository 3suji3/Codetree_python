N = int(input())

num = 0 

for i in range(N):
    print('  ' * i, end='')

    for j in range(N - i):
        print(chr(num + ord('A')), end=' ')
        num = (num + 1) % 26

    print()