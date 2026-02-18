arr = [list(input().split()) for _ in range(3)]

cnt = 0

if arr[0][0] == 'Y' and int(arr[0][1]) >= 37:
    cnt += 1

if arr[1][0] == 'Y' and int(arr[1][1]) >= 37:
    cnt += 1

if arr[2][0] == 'Y' and int(arr[2][1]) >= 37:
    cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')
