str = ['apple', 'banana', 'grape', 'blueberry', 'orange']

char = input()

str2 = []

cnt = 0

for i in str:
    if i[2] == char or i[3] == char:
        print(i)
        cnt += 1
print(cnt)