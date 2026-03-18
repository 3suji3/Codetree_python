a, b = map(int, input().split())

for i in range(1, 10):
    line = []
    for j in range(b, a-1, -1):
        if j % 2 == 0:
            line.append(f"{j} * {i} = {i * j}")
    print(" / ".join(line))