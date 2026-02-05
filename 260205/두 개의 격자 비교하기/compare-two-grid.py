n, m = map(int, input().split())

arr1 = [[int(j) for j in input().split()] for _ in range(n)]
arr2 = [[int(j) for j in input().split()] for _ in range(n)]

for i in range(m):
    for j in range(n):
        if arr1[i][j] == arr2[i][j]:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()