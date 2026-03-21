N = int(input())

for i in range(1, N+1):
    for j in range(1, N - i + 2):
        elif j == N - i + 1:
            print(f"{i} * {j} = {i*j}", end=" ")
        else:
            print(f"{i} * {j} = {i*j} /", end=" ")