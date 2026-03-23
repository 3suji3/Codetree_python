start, end = map(int, input().split())

count = 0

for n in range(start, end + 1):
    if n == 1:
        continue

    div_sum = 1

    i = 2
    while i * i <= n:
        if n % i == 0:
            div_sum += i
            if i != n // i:
                div_sum += n // i
        i += 1

    if div_sum == n:
        count += 1

print(count)