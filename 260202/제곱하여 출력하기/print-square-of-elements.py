N = int(input())

num1 = []
num2 = []

num1 = list(map(int, input().split()))

for i in num1:
    num2 = i ** 2
    print(num2, end=" ")

