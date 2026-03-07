N = int(input())

# 첫 줄
print("* " * N)

star = N // 2
blank = 2

while star > 0:
    # 현재 star 개수를 몇 줄 출력할지 결정
    # 맨 처음 star == N//2 는 1번만 출력
    # 그 다음부터는 2번씩 출력
    if star == N // 2:
        repeat = 1
    else:
        repeat = 2

    for _ in range(repeat):
        if star == 1:
            print(" " * blank + "*")
        else:
            print(" " * blank + ("*   " * (star - 1)) + "*")

    star -= 1
    blank += 4